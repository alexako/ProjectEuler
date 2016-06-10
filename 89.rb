#!/usr/bin/ruby


def load_file(file)
    content = []
    File.open(file, "r") do |f|
        f.each_line do |line|
            content << line
        end
    end
    return content
end

def convert_to_arab(num)
    val = 0
    last_digit = "M"
    num.split("").each do |i|
        if $conversion[i] #Skip nil values in string
            if $conversion[last_digit] < $conversion[i]
                val -= $conversion[last_digit]
                val += $conversion[i] - $conversion[last_digit]
            else
                val += $conversion[i]
            end
        end
        last_digit = i
    end
    return val
end

def convert_to_rom(num)
    @roman_numerals = []
    $conversion.each do |rom, den|
        if num / den
            count = num / den
            for i in 1..count
                (@roman_numerals ||= []) << rom
            end
            num = num % den
        end
    end
    return minimalize(@roman_numerals.join)
end

def minimalize(num)
    replacements = Hash[
        "IIIII" => "V",
        "VIIII" => "IX",
        "IIII" => "IV",
        "VV" => "X",
        "LXXXX" => "XC",
        "XXXXX" => "L",
        "XXXX" => "XL",
        "LL" => "C",
        "DCCCC" => "CM",
        "CCCCC" => "D",
        "CCCC" => "CD",
        "DD" => "M"
    ]
    replacements.each do |key, value|
        while num.include?(key)
            the_butt = num[num.index(key)+key.length..num.length]
            num.slice!num[num.index(key)..num.length]
            num << value + the_butt
        end
    end
    return num
end


#Main
filename = "p089_roman.txt"
roman_nums = load_file(filename)
$conversion = Hash[
    "M" => 1000,
    "D" => 500,
    "C" => 100,
    "L" => 50,
    "X" => 10,
    "V" => 5,
    "I" => 1
]

total_saved = 0

roman_nums.each do |line|
#    ar = convert_to_arab(line)
#    ro = convert_to_rom(ar)
    size = line.length
    if size > minimalize(line).length
        saved = size - minimalize(line).length
        puts "#{line}: #{size} - #{minimalize(line)}: #{minimalize(line).length}"
        puts "Number of chars saved: #{saved}\n\n"
        total_saved += saved
    end
end

puts "Total number of characters saved: #{total_saved}"
