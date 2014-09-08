def hasProperty(num)
    # Splices
    for i in 1..$div.length
        puts "#{num[i]}, #{num[i+1]}, #{num[i+2]} div #{$div[i-i]}"
        if num[i+2]
            unless ((num[i] + num[i+1] + num[i+2]).to_i % $div[i-1] == 0)
                return false
            end
        end
    end
    return true
end

#Get all pandigital numbers
def get_pandigitals
    return (0..9).to_a.permutation.map(&:join)
end


#Main
puts "Started!"
$div = [2, 3, 5, 7, 11, 13, 17]
$pans = get_pandigitals
puts "Got list of permutations!"

puts "Cleaning list of invalid ints..."
#Remove strings starting with '0'
$pans.delete_if { |x| x[0] == '0' }
puts "Cleaned list!"

puts "Finding appropriate ints..."
#Find int with property
$pans.each do |i|
    if hasProperty(i)
        puts "Found! #{i}"
        ($pans_sum ||= []) << i.to_i
    end
end

if $pans_sum
    puts "Answer found: #{$pans_sum.inject(:+)}"
else
    puts "No answer found."
end
