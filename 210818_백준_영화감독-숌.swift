import Foundation
func main() {
    let n = Int(readLine()!)!
    var i = 665
    var count = 0
    var title = 0
    while true {
        i += 1
//        let j = "\(i)"
//        guard j.contains("666") else { continue }
        var temp = i
        var count6 = 0
        while temp > 0 {
            if temp % 10 == 6 {
                count6 += 1
            } else {
                count6 = 0
            }
            
            if count6 == 3 {
                count += 1
                break
            }
            
            temp /= 10
        }
        
        if count == n {
            title = i
            break
        }
    }
    print(title)
}
main()


