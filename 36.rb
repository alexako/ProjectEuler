#!/usr/bin/ruby


sum = 0
for i in 1..1000000
    base10 = i.to_s
    base2 = i.to_s(2)
    rbase10 = base10.reverse
    rbase2 = base2.reverse
    if base2[0] != '0' || base2[-1] != '0'
        if base10 == rbase10 && base2 == rbase2
            puts "Found! #{i} = #{i.to_s(2)}"
            sum += i
        end
    end
end

puts "Total sum: #{sum}"
