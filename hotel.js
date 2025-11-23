const mongoose = require('mongoose');

// MongoDB connection string (update with your MongoDB URI)
const dbURI = 'mongodb://localhost:27017/hotels'; // Replace 'localhost:27017' with your server URI if different

// Connect to the MongoDB database
mongoose.connect(dbURI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
    .then(() => console.log('Connected to the hotels database'))
    .catch(err => console.error('Database connection error:', err));

// Define the schema for the hotels collection
const hotelSchema = new mongoose.Schema({
    name: { type: String, required: true }, // Hotel name
    destination: { type: String, required: true }, // Destination or location
    price: { type: Number, required: true }, // Price per night
    available: { type: Boolean, required: true, default: true }, // Default availability is true
    rating: { type: Number, min: 0, max: 5, default: 0 }, // Default rating is 0, range is 0 to 5
    reviews: [{
        reviewer: { type: String, required: true }, // Reviewer's name
        comment: { type: String, required: true },  // Review comment
        date: { type: Date, default: Date.now } // Review date, default to now
    }],
    pictures: { type: [String], default: [] } // Array of picture URLs, default to an empty array
}, {
    timestamps: true // Automatically adds createdAt and updatedAt fields
});

// Create the Mongoose model for hotels
const hotels = mongoose.model('hotels', hotelSchema);

// Export the model for use in other files
module.exports = hotels;
