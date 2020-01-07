from __future__ import absolute_import


class AverageMeter(object):
    """Computes and stores the average and current value"""

    def __init__(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

# if (i + 1) % cfg.print_freq == 0:
#                 print('Epoch: [{}][{}/{}]\t'
#                       'Time {:.3f} ({:.3f})\t'
#                       'Data {:.3f} ({:.3f})\t'
#                       'Loss {:.3f} ({:.3f})\t'
#                       'Prec {:.2%} ({:.2%})\t'
#                       .format(epoch, i + 1, len(train_loader),
#                               batch_time.val, batch_time.avg,
#                               data_time.val, data_time.avg,
#                               losses.val, losses.avg,
#                               precisions.val, precisions.avg))