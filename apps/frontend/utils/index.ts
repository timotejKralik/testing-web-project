import parse from "node-html-parser";
import { META_DESCRIPTION_MAX_LENGTH } from "constants/index";


export function truncate(string: string, maxLength: number) {
  const truncationString = "This is so long, truncating.";
  return (string.length > maxLength) ? string.slice(0, maxLength - truncationString.length) + truncationString : string;
};
export const getMetaDescriptionFromContent = (content: string) => {
  return truncate(parse(content).textContent, META_DESCRIPTION_MAX_LENGTH);
}