def confusion_matrix(y_true, y_pred):
    '''
    calculates the confusion matrix

    parameters:
        y_true (list): A list with the true values as in,
                                0 - negative
                                1 - positive

        y_pred (list): A list with the predictions as in,
                                0 - negative
                                1 - positive
    returns:
        cm (list): A list with the values for TN, FP, FN, TP (true negatives, false positives, false negatives and false positives)
    '''
    cm = [0, 0, 0, 0] # tn, fp, fn, tp
    for y, y_hat in zip(y_true, y_pred):
        if(y == 0): # false
            if(y_hat == 0):
                cm[0] += 1 # tn
            else:
                cm[1] += 1 # fp
        elif(y == 1): # true
            if(y_hat == 0):
                cm[2] += 1 # fn
            else:
                cm[3] += 1 # tp
                
    return cm

def calculate_metrics(y_attack_types, y_pred, threshold=0.5):
    '''
    calculates the metrics APCER, BPCER and ACER as defined for the OULU dataset.

    parameters:
        y_attack_types (list): A list with the labels for the samples as in,
                                1 - live samples
                                2 - print attack 1
                                3 - print attack 2
                                4 - display attack 1
                                5 - display attack 2

        y_pred_display (list): A list with the predictions as in,
                                0 - attack
                                1 - live

                                or

                                [0-1] float binarized if threshold bellow

        pred_threshold (int) [0-1]: used to binarize predictions

    returns:
        apcer (float) [0-1] attack presentation classification error rate
        bpcer (float) [0-1] bona fide presentation classification error rate
        acer (float) [0-1] average classification error rate
    '''
    
    y_pred = [(0 if y >= threshold else 1) for y in y_pred] # binarize y_pred using threshold
    y_true = [(0 if y == 1 else 1) for y in y_attack_types] # get y_true from the y_attack_types
    
    # from now on 1=attack and 0=live
    
    print_attack_indices = [index for index, element in enumerate(y_attack_types) if element in [1,2,3]]
    display_attack_indices = [index for index, element in enumerate(y_attack_types) if element in [1,4,5]]
        
    y_true_print_attack = [y_true[i] for i in print_attack_indices]
    y_pred_print_attack = [y_pred[i] for i in print_attack_indices]
    y_true_display_attack = [y_true[i] for i in display_attack_indices]
    y_pred_display_attack = [y_pred[i] for i in display_attack_indices]
        
    # tn, fp, fn, tp
    cm_print_attack = confusion_matrix(y_true_print_attack, y_pred_print_attack) # confusion matrix for print attack
    cm_display_attack = confusion_matrix(y_true_display_attack, y_pred_display_attack) # confusion matrix for display attack
    
    try:
        apcer_print = cm_print_attack[2] / (cm_print_attack[3] + cm_print_attack[2]) # fn / (tp + fn)
    except:
        apcer_print = 0.0
    
    try:
        apcer_display = cm_display_attack[2] / (cm_display_attack[3] + cm_display_attack[2]) # fn / (tp + fn)
    except:
        apcer_display = 0.0

    try:
        bpcer_print = cm_print_attack[1] / (cm_print_attack[1] + cm_print_attack[0]) # fp/(fp + tn)
    except:
        bpcer_print = 0.0

    try:
        bpcer_display = cm_display_attack[1] / (cm_display_attack[1] + cm_display_attack[0]) # fp/(fp + tn)
    except:
        bpcer_display = 0.0

    apcer = max(apcer_print, apcer_display) # max of both apcer (print, display) attack presentation classification error rate
    bpcer = max(bpcer_print, bpcer_display) # max of both bpcer (print, display) bona fide presentation classification error rate
    
    acer = (apcer + bpcer) / 2 # average between apcer and bpcer

    return apcer, bpcer, acer