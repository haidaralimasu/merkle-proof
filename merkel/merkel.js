const keccak256 = require("keccak256");
const { MerkleTree } = require("merkletreejs");

let whitelisted = [
  "0xA9889aAC1c8d0e8d5F874CdC9D475D0Dfcf32EB1",
  "0xF9eF71BF3F5834BB75C9DD20E041bDfEbE931fD2",
  "0xDf9f0593449Ec6e6a3706EBB505794FdB83FEF77",
];

let leafNodes = whitelisted.map((addr) => keccak256(addr));
let merkleTree = new MerkleTree(leafNodes, keccak256, { sortPairs: true });

const rootHash = merkleTree.getRoot();

console.log(merkleTree.toString());

const address = leafNodes[0];

const hexProof = merkleTree.getHexProof(address);

console.log(hexProof);
