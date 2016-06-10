#!/usr/bin/ruby


def generate_pandigitals
    return (1..9).to_a.permutation.map(&:join)
end

def is_pand(num)
    for j in 3..6
        for i in 0..j
            if num[0..i].to_i * num[i+1..j].to_i == num[j+1..8].to_i
                puts "Found! #{num[0..i]} * #{num[i+1..j]} = #{num[j+1..8]}"
                return num[j+1..num.length].to_i
            end
        end
    end
    return nil
end


#Main
puts "Generating pandigitals..."
pans = generate_pandigitals
puts "Done!"
pand_prod = []

pans.each do |x|
    if is_pand(x)
        if not pand_prod.include?(is_pand(x))
            pand_prod << is_pand(x)
        end
    end
end

puts pand_prod
puts "Answer found: #{pand_prod.inject{|sum,x| sum + x}}"
