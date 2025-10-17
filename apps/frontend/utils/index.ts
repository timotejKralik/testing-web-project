import parse from "node-html-parser";
import { META_DESCRIPTION_MAX_LENGTH } from "constants/index";


export function truncate(string: string, maxLength: number) {
  const truncationString = 'This is so long, truncating.';
  if (string.length > maxLength) {
    const availableLength = maxLength - truncationString.length;
    if (availableLength <= 0) {
      // If maxLength is too small to fit the truncation string, just return the truncation string
      return truncationString.slice(0, maxLength);
    }
    return string.slice(0, availableLength) + truncationString;
  }
  return string;
};
export const getMetaDescriptionFromContent = (content: string) => {
  return truncate(parse(content).textContent, META_DESCRIPTION_MAX_LENGTH);
}