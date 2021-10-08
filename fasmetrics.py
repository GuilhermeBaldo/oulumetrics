import numpy as np
from sklearn.metrics import confusion_matrix

class OuluEvaluation():
    
    def __init__(self):
        pass

    def fas_metrics(self, y_pred_print, y_true_print, y_pred_display, y_true_display):
        pass

def fas_metrics(y_pred_print, y_true_print, y_pred_display, y_true_display):

    metrics = {}

    tn_print, fp_print, fn_print, tp_print = confusion_matrix(y_true_print, y_pred_print).ravel()
    tn_display, fp_display, fn_display, tp_display = confusion_matrix(y_true_display, y_pred_display).ravel()

    metrics['far_print'] = fn_print / (tp_print + fn_print) if (tp_print + fn_print) != 0 else 0 # false acceptance rate for print attack
    metrics['far_display'] = fn_display / (tp_display + fn_display) if (tp_display + fn_display) != 0 else 0# false acceptance rate for display attack

    metrics['frr_print'] = fp_print / (fp_print + tn_print) if (fp_print + tn_print) != 0 else 0 # false rejection rate for print attack
    metrics['frr_display'] = fp_display / (fp_display + tn_display) if (fp_display + tn_display) != 0 else 0# false rejection rate for display attack

    metrics['apcer'] = np.max([metrics['far_print'], metrics['far_display']]) # attack presentation classification error rate
    metrics['bpcer'] = np.max([metrics['frr_print'], metrics['frr_display']]) # bona fide presentation classification error rate
    metrics['acer'] = np.mean([metrics['apcer'], metrics['bpcer']]) # average classification error rate

    return metrics

if __name__ == "__main__":

    # 0 - attack, 1 -  real
    k = 10
    y_pred_print = np.random.randint(2, size=k)
    y_true_print = np.random.randint(2, size=k)
    y_pred_display = np.random.randint(2, size=k)
    y_true_display = np.random.randint(2, size=k)
    print(fas_metrics(y_pred_print, y_true_print, y_pred_display, y_true_display))

    
