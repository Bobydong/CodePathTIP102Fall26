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

 
if __name__ == "__main__":
    nums = [3, 2, 1, 4]
    print(goldilocks_approved(nums))

    nums = [1, 2]
    print(goldilocks_approved(nums))

    nums = [2, 1, 3]
    print(goldilocks_approved(nums))
    # sentence = "tubby little cubby all stuffed with fluff"
    # reverse_sentence(sentence)

    # sentence = "Pooh"
    # reverse_sentence(sentence)