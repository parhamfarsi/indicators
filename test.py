import analysis
def test(all_data):
    # get predicted signals
    predicted = analysis.analyze_indicators(all_data)
    
    # get true labels
    true_labels = all_data['label']
    
    # make sure lengths match
    n = min(len(predicted), len(true_labels))
    
    correct = 0
    total = 0
    
    for i in range(n):
        if predicted[i] is None:  # skip days without signal
            continue
        if predicted[i] == true_labels[i]:
            correct += 1
        total += 1
    
    accuracy = correct / total if total > 0 else 0
    return accuracy
