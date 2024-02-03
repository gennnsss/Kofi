const product = [
    {
        id: 0,
        image: 'image/vanilla-chocolate-mocha.jpg',
        title: 'Chocolate Cream Cold Brew',
        price: 120,
    },
    {
        id: 1,
        image: 'image/vanilla-chocolate-mocha.jpg',
        title: 'Cinnamon Caramel Cream Cold Brew',
        price: 150,
    },
    {
        id: 2,
        image: 'image/about.png',
        title: 'Cold Brew Coffee with Milk',
        price: 100,
    },
    {
        id: 3,
        image: 'image/aa-1.jpg',
        title: 'Cold Brew',
        price: 90,
    },
    {
        id: 4,
        image: 'image/about.png',
        title: 'Pumpkin Cream Cold Brew        ',
        price: 130,
    },
    {
        id: 5,
        image: 'image/about.png',
        title: 'Salted Caramel Cream Cold Brew        ',
        price: 120,
    },
    {
        id: 6,
        image: 'image/about.png',
        title: 'Vanilla Sweet Cream Cold Brew'        ,
        price: 140,
    },
    {
        id: 7,
        image: 'image/about.png',
        title: 'Cold Brew Coffee        ',
        price: 100,
    },
];
const categories = [...new Set(product.map((item)=>
    {return item}))]
    let i=0;
document.getElementById('root').innerHTML = categories.map((item)=>
{
    var {image, title, price} = item;
    return(
        `</div>
        <div class='bottom'>
        <p>${title}</p>
        <h2>₱ ${price}.00</h2>`+
        "<button onclick='addtocart("+(i++)+")'>Add to cart</button>"+
        `</div>
        </div>`
    )
}).join('')

var cart =[];

function addtocart(a){
    cart.push({...categories[a]});
    displaycart();
}
function delElement(a){
    cart.splice(a, 1);
    displaycart();
}

function displaycart(){
    let j = 0, total=0;
    document.getElementById("count").innerHTML=cart.length;
    if(cart.length==0){
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("total").innerHTML = "₱ "+0+".00";
    }
    else{
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {
            var {image, title, price} = items;
            total=total+price;
            document.getElementById("total").innerHTML = "₱ "+total+".00";
            return(
                `<div class='cart-item'>
                <p style='font-size:12px;'>${title}</p>
                <h2 style='font-size: 15px;'>₱${price}.00</h2>`+
                "<i class='fa-solid fa-trash' onclick='delElement("+ (j++) +")'></i></div>"
            );
        }).join('');
    }
}

