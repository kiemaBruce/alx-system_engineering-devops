#!/usr/bin/env ruby
if ARGV.length > 0
	puts ARGV[0].scan(/hbt{2,5}n/).join
end
