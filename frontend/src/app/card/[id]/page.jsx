import {CardWithBanner} from "@/components/CardWithBanner/CardWithBanner";
import cn from "classnames";
import styles from "./page.module.scss"
import {notFound} from "next/navigation";
import {CardWithoutBanner} from "@/components/CardWithoutBanner/CardWithoutBanner";

async function getData(id) {
  const response = await fetch(`http://37.49.209.63:1300/card/${id}`, {next: {revalidate: 30}});

  if (!response.ok) {
    return notFound();
  }

  return response.json();
}

const CardPage = async ({params}) => {
  const data = await getData(params.id);
  data.image = `http://37.49.209.63:1300/images/${data.id}.jpg`

  return <div className={cn("container", styles.container)}>
    {data.type == 1 && <CardWithoutBanner data={data}/>}
    {data.type == 2 && <CardWithBanner data={data}/>}
  </div>;
};

export default CardPage;
