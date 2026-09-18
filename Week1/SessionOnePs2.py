def reverse_sentence(sentence):
    words = sentence.split()
    ret = ""
    words.reverse()
    for word in words:
        ret += word + " " 
    print(ret)

def goldilocks_approved(nums):
    if (len(nums) <= 2):
        return -1
    maxval = max(nums)
    minval = min(nums)

    # iterate through the list
    for num in nums:
        if (num != min and num != max):
            return num
    return -1
    # find and keep track of the absolute max and min in the list
    # iterate through the list a second time
    # return the  first number that isn't a max or min



def delete_minimum_elements(hunny_jar_sizes):
    """
    Given a list of integers, write a function  that continuously removes the minimum element until the list is empty. 
    Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.
    """
    # go over input, output  
    # edge case: list is empty --> return an empty list
    # constraint: proactively manage original array elements 

    # create new list
    ret = []
    # handle edge case
    if (len(hunny_jar_sizes) == 0):
        return ret
    # while the list isn't empty
    while len(hunny_jar_sizes) != 0:
    #   find the minimum element
        minimum = min(hunny_jar_sizes)
    #   append it to new list
        ret.append(minimum)
    #   delete from the orignal list
        hunny_jar_sizes.remove(minimum) # note: removes only 1 instance
    # return new list 
    return ret

def final_value_after_operations(operations):
    tiger = 1
    for op in operations:
        if (op == "bouncy" or op == "flouncy"):
            tiger += 1
        if (op == "trouncy" or op == "pouncy"):
            tiger -= 1
    return tiger

    
    

if __name__ == "__main__":
    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))

    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))


    # hunny_jar_sizes = [5, 3, 2, 4, 1]
    # print(delete_minimum_elements(hunny_jar_sizes))

    # hunny_jar_sizes = [5, 2, 1, 8, 2]
    # print(delete_minimum_elements(hunny_jar_sizes))

    # nums = [3, 2, 1, 4]
    # print(goldilocks_approved(nums))

    # nums = [1, 2]
    # print(goldilocks_approved(nums))

    # nums = [2, 1, 3]
    # print(goldilocks_approved(nums))
    # sentence = "tubby little cubby all stuffed with fluff"
    # reverse_sentence(sentence)

    # sentence = "Pooh"
    # reverse_sentence(sentence)