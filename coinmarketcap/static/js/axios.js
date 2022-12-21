$(document).ready(function () {
    const getBtn = document.getElementById("get-coins")
    // document.addEventListener('keydown',(Event)=>{
    //     console.log(Event.key)
    //     console.log(Event.code)
    // })
    $(document).on('input','.input-class',function(){    
        var input = $('#input-id')
        let inputValue = input.val()
        // let res = inputValue.replace(/^\s+|\s+$/gm,'');
        // let res = inputValue.trim();
        let inputResult = inputValue.split(' ').join('');
        $('#input-id',).val(inputResult);
        async function axiosfunction(){  // , { params: { name_or_symbol: inputResult } }
            const result = await axios.get(`http://127.0.0.1:8000/coin/api/get-coin/${inputResult}`);
            var contents = "";
            for (let i = 0; i < result.data.length; i++){
                const coin = result.data[i]
                contents += `
                <dl>
                    <br>
                    <dt><a href="http://127.0.0.1:8000/coin/get-coin/${coin.symbol}" target='_blank'><strong>${coin.name}</strong></a></dt>
                        <dd>${coin.price}</dd>
                        <dd>${coin.symbol}</dd>
                </dl>`
                $(".all-coins").html(contents)
                
            } 
        }
        axiosfunction()
    })





    const getCoins = () => {
        
        axios.get('http://127.0.0.1:8000/coin/api/get-coins/').then(res =>{
            var contents = "";
            var coins = res.data;
            for (let i = 0; i < coins.length; i++){
                const coin = coins[i]
                // console.log(coin.symbol)
                contents += `
                <dl>
                    <br>
                    <dt><a href="http://127.0.0.1:8000/coin/get-coin/${coin.symbol}" target='_blank'><strong>${coin.name}</strong></a></dt>
                        <dd>${coin.price}</dd>
                        <dd>${coin.symbol}</dd>
                </dl>`
            } 
            $(".all-coins").html(contents)
        });
    };

    getBtn.addEventListener('click',getCoins);

})




// const getCoins1 = ()  => {
//     axios({
//         method: 'get',
//         url: 'http://127.0.0.1:8000/coin/get-coins/',
//         data: { 'prop': 'value' },
//         headers: {
//             'Content-Type':'application/json'
//         }
//       }).then(res => {
//         console.log(res)
//       });
// }