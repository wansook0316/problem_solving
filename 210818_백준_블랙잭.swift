import Foundation

func combination<T>(_ elements: [T], _ k: Int) -> [[T]] {
    var result = [[T]]()
    
    func combi(_ index: Int, _ now: [T]) {
        if now.count == k {
            result.append(now)
            return
        }
        for i in index..<elements.count {
            combi(i + 1, now + [elements[i]])
        }
    }
    combi(0, [])
    return result
}

func main() {
    let input = readLine()!
    let seps = input.components(separatedBy: " ")
    let n = Int(seps[0])!, m = Int(seps[1])!
    var cards = [Int]()
    
    cards = readLine()!.components(separatedBy: " ").map { Int($0)! }
    
    
    print(combination(cards, 3).map({ $0.reduce(0, { $0 + $1 })}).filter({ $0 <= m }).max()!)
    
}

main()