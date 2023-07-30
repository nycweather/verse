"use client";
import { useEffect, useState } from "react";

function Index() {
  const [data, setData] = useState("Loading...");
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8080/");
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setData(data.message);
        console.log(data); // Log the updated data here
      } catch (error) {
        console.error("Error fetching data:", error);
        // Handle error states here if necessary
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>{data}</h1>
    </div>
  );
}

export default Index;
