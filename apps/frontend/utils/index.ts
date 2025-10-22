import parse from "node-html-parser";
import { META_DESCRIPTION_MAX_LENGTH } from "constants/index";


export function truncate(string: string, maxLength: number) {
  if (maxLength <= 0) return '';
  if (string.length <= maxLength) return string;
  const ellipsis = '...';
  const sliceEnd = Math.max(0, maxLength - ellipsis.length);
  return string.slice(0, sliceEnd) + ellipsis;
};
export const getMetaDescriptionFromContent = (content: string) => {
  return truncate(parse(content).textContent, META_DESCRIPTION_MAX_LENGTH);
}