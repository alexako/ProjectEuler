def isPandigital(num)
    for i in 0..9
        unless (num.to_s.include?(i.to_s))
            return false
        end
    end
    return true
end

def hasProperty(num)

    # Create str array from int
    num.to_s.each_char do |i|
        (@s_num ||= []) << i
    end

    # Splices
    div = [2, 3, 5, 7, 11, 13, 17]
    for i in 1..div.length
        unless ((@s_num[i] + @s_num[i+1] + @s_num[i+2]).to_i % div[i-1] == 0)
            return false
        end
        puts "#{@s_num[i..i+2]}, div = #{div[i-1]}"
    end
    return true
end


#Main
#i = 1406357289
#for i in 1406357270..1406357390
for i in 1000000000..9999999999
    if i % 212311 == 0
        puts "Trying #{i}..."
    end
    if isPandigital(i)
       if hasProperty(i)
           puts "Found! #{i}"
           ($pans ||= []) << i
       end
    end
end

if $pans
    puts "Answer found: #{$pans.inject(:+)}"
else
    puts "No answer found."
end
