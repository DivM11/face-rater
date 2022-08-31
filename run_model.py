import torchvision.transforms as transforms
from PIL import Image

from modeling.create_model import AlexNet
from modeling import torch_convert


def add_rating(image_path=None, img=None):
    # net definition 
    net = AlexNet()#.cuda()
    # load pretrained model
    model = torch_convert.load_model('modeling/saved_models/alexnet.pth')
    state_dict = torch_convert.byte_convert(model)['state_dict']
    net.load_state_dict(state_dict)

    # evaluate
    net.eval()

    # loading data...
    transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),])
    if img is None:
        img = Image.open(image_path).convert('RGB')
    img = transform(img)
    img = img.unsqueeze(0)#.cuda(non_blocking=True)
    output = net(img).squeeze(1).item()
    print("Face Rating out of 5:", output)
    return output


if __name__ == '__main__':
    add_rating(image_path="stest.jpg")