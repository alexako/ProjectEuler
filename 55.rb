#!/usr/bin/ruby


def is_palindrome(num)
    r_num = num.to_s.reverse
    return num.to_s == r_num
end

def is_lychrel(num)
    puts "Start #{num}"
    limit = 1
    while limit < 50
        r_num = num.to_s.reverse!.to_i
        sum = num + r_num
        if is_palindrome(sum)
            return false 
        end
        limit += 1
        num = sum
    end
    puts "Found a Lychrel number | iterations: #{limit}"
    return true 
end


#Main
count = 0

for i in 1..10000
    if is_lychrel(i)
        count += 1
    end
end

puts "Count: #{count}"
