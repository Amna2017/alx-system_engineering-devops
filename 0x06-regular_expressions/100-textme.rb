#!/usr/bin/env ruby
#my 100 ruby regex
puts ARGV[0].scan(/(?<=from:|to:|flags:)[+-]?\S+(?=\])/).join(",")
