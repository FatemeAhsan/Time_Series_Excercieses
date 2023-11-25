import logging
import time

from d2l.d2l import torch as d2l
from syne_tune import Reporter
from argparse import ArgumentParser

import torch
from torch import nn

if __name__ == '__main__':
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    parser = ArgumentParser()
    parser.add_argument('--learning_rate', type=float)
    parser.add_argument('--batch_size', type=int)
    parser.add_argument('--max_epochs', type=int)

    args, _ = parser.parse_known_args()
    report = Reporter()

    num_classes = 2
    
    m2_model = torch.hub.load('pytorch/vision', 'mobilenet_v2', pretrained=True)
    m2_model.classifier[1] = torch.nn.Linear(in_features=m2_model.classifier[1].in_features,
                                             out_features=num_classes)

    nn.init.xavier_uniform_(m2_model.classifier[1].weight)

    model = d2l.CustomClassifier(m2_model, lr=args.learning_rate)
    trainer = d2l.HPOTrainer(max_epochs=1, num_gpus=1)
    data = d2l.Mobile_Phone_Hands(batch_size=args.batch_size)

    for step in range(args.max_epochs):
        time.sleep(0.1)
        if step == 0:
            # Initialize the state of Trainer
            trainer.fit(model=model, data=data)
        else:
            trainer.fit_epoch()

        validation_error = trainer.validation_error().cpu().detach().numpy()
        report(epoch=step + 1, validation_error=float(validation_error))
