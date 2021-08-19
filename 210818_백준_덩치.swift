
import Foundation

class Guy {
    let id: Int
    var rank: Int = 0
    let height: Int
    let weight: Int
    
    init(id: Int, height: Int, weight: Int) {
        self.id = id
        self.height = height
        self.weight = weight
    }
}

func main() {
    let n = Int(readLine()!)!
    var guys = [Guy]()
    (1...n).forEach {
        let seps = readLine()!.components(separatedBy: " ").map { Int($0)! }
        guys.append(Guy(id: $0, height: seps[1], weight: seps[0]))
    }
    let compare: (Guy, Guy) -> Bool = { $0.height > $1.height && $0.weight > $1.weight }
    
    for now in guys {
        var rank = 1
        for other in guys {
            if now === other { continue }
            if compare(other, now) == true {
                rank += 1
            }
        }
        now.rank = rank
    }
    
    print(guys.sorted(by: { $0.id < $1.id }).map({ "\($0.rank)" }).joined(separator: " "))
}

main()


