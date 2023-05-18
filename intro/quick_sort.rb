def quick_sort(array)
    return array if array.length <= 1
    # how it works: you iterate through the array, putting each element small than the first into a
    # smaller-than array, and each element bigger than it into a bigger-than array
    # then make recursive calls to quick_sort and let recursion magic do it's thing.

    # first things first, we want to grab the very first element and two arrays

    element = array.shift()
    less_than = []
    greater_than = []

    array.each do |number|
        if number <= element
            less_than.push(number)
        else
            greater_than.push(number)
        end
    end

    return quick_sort(less_than) + [element] + quick_sort(greater_than)
end

print(quick_sort([5,3,1,6,7,8,8,3,7]))