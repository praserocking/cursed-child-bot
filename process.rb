require 'set'
require 'json'

content = File.read("harry.txt")

acts = content.gsub("\t", " ").gsub("\f", "").split("ACT").map{|i| i.split("\n")}

noise_actors = Set.new

corpus = []
acts.each do |act|
	act_exchanges = []
	act.each do |exchange|
		exc = exchange.split(":")[1] if exchange.include? ":"
		act_exchanges << exc.lstrip.rstrip unless exc.nil?
	end
	corpus << act_exchanges unless act_exchanges.size == 0
end

File.write("corpus.json", corpus.to_json)


