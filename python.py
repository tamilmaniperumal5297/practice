def is_memory_high(used_gb, total_gb):
    percentage = used_gb/total_gb * 100
    if percentage > 80:
        return True
    else:
        return False

used = 10
total = 20
memory = is_memory_high(used, total)
print(f"Is memory usage high? {memory}")
    