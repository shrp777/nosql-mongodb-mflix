import { MongoClient } from "mongodb";

const uri = process.env.MONGODB_URL;
const dbName = process.env.MONGO_INITDB_DATABASE;
const collectionName = process.env.MONGO_INITDB_COLLECTION;

const client = new MongoClient(uri);

async function run() {
  try {
    const database = client.db(dbName);
    const movies = database.collection(collectionName);

    const query = { title: "Back to the Future" };
    const movie = await movies.findOne(query);

    console.log(movie.title); //"Back to the Future"
  } catch (error) {
    console.error(error);
  } finally {
    await client.close();
  }
}
run();
