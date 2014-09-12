#!/usr/bin/ruby


def sqr_sum(num)
    sum = 0
    num = num.to_s
    for i in 0..num.length
        sum += num[i].to_i * num[i].to_i
    end
    return sum
end

def end_89(num)
    chain = [num.to_i]
    current = num
    while true
        current = sqr_sum(current)
        if current == 1 or current == 89
            if chain.include?(1) 
                return false
            end
            if chain.include?(89)
                chain << current
                puts "Chain found! #{chain}"
                return true
            end
        end
        chain << current
    end
end

#Main
count = 0
for i in 1..10000000
    if end_89(i.to_s)
        count += 1
    end
end

puts "Answer found: #{count}"
