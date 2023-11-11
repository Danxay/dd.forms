import { CardWithoutBanner } from "@/components/CardWithoutBanner/CardWithoutBanner";
import { CardWithBanner } from "@/components/CardWithBanner/CardWithBanner";
import cn from "classnames";
import styles from "./page.module.scss"

async function getData(id) {
  // const response = await fetch(`http://localhost:3000/api/projects/${id}`, {next: {revalidate: 30}});

  // if (!response.ok) {
  //   return notFound();
  // }
  //
  // return response.json();

  const response = {
    image: "https://i1.sndcdn.com/artworks-nbXEtIsuHFab90iU-mPzLmw-t500x500.jpg",
      name: "Дарья Шиханова",
      bio: "event-менеджер в компании",
      links: {"vk": "https://vk.com", "tg": "https://t.me"},
      phone: null,
      email: "erger@mail.ru"
  }

  return response
}

const CardPage = async ({params}) => {
  const data = await getData(params.id);

  return <div className={cn("container", styles.container)}><CardWithBanner image={data.image} name={data.name} bio={data.bio} links={data.links} phone={data.phone} email={data.email}/></div>;
};

export default CardPage;
