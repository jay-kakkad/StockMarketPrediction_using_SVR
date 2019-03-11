var express 		=require("express"),
	bodyParser 		=require("body-parser"),
	methodOverride 	=require("method-override"),
	expressSanitizer=require("express-sanitizer"),
	app				=express();

app.engine('html', require('ejs').renderFile);
app.set("view engine","html");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: true}));
app.use(methodOverride("_method"));
app.use(expressSanitizer());

//RESTFUL ROUTES
app.get("/", function(req,res){
    res.render("login.html");
});

//GET ROUTE FOR LOGIN PAGE
app.get("/login",function(req,res){
	res.render("login.html");
});

//GET ROUTE FOR DASHBOARD PAGE
app.get("/dashboard",function(req,res){
	res.render("index.html");
});

//GET ROUTE FOR PROFILE PAGE
app.get("/profile",function(req,res){
	res.render("profile.html");
});


//GET SHOW ROUTE FOR PROFILE PAGE
app.get("/profile/:id",function(req,res){
	res.send("Here all the profiles will be displayed:");
});

//GET EDIT ROUTE FOR PROFILE PAGE
app.get("/profile/:id/edit",function(req,res){
	res.send("Here I will edit the profile");
});

//CREATE PROFILE AT PROFILE PAGE
app.post("/profile",function(req,res){
	res.send("Here are my post requests going....");
});

//UPDATE PROFILE AT PROFILE PAGE
app.put("/profile/:id",function(req,res){
	res.send("Profile page will be edited here");
});

//DELETE PROFILE AT PROFILE PAGE
app.delete("profile/:id",function(req,res){
	res.send("OOPS!!YOUR PROFILE WILL BE DELETED SOON!!");
});

//GET ROUTE FOR CONTACT PAGE
app.get("/contact",function(req,res){
	res.render("contact.html");
});

//GET ROUTE FOR CHARTS PAGE
app.get("/charts",function(req,res){
	res.render("charts.html");
});

//CONNECT TO BACKEND SERVER
app.listen(3000,function(){
	console.log("The Server has started running....");
});	

