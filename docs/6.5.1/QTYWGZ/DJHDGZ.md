<p>本文例举了一些常用的报价操作所对应的回调规则。在给定交易所报价回报顺序的前提下，CTP返回给API的回调顺序是固定的。</p>
<p>特别要注意，大商所只返回一次报价状态回报，例如一笔报价从报入到未成交到最终成交，一共有三个状态，但是大商所只推送未成交报价回报，全部成交后不推送成交报价回报。甚至在查询报价时，其报价状态也仍然是未成交状态。用户在测试和实现自己业务的时候要格外注意这点。</p>
<p>目前国内几家交易所的报价规则各不相同，本文不做详细例举，希望大家在梳理规则时学会举一反三。</p>
<span class="anchor" id="d79d657f-bca5-4f02-a2e7-6b3497d9b8e7"></span>
## 1.术语说明
<ul>
<li>报价衍生单</li>
</ul>
<p>报价报入交易所时，同时会衍生出两笔买卖报单，以普通报单的形式报入交易所。这两笔报单称之为报价衍生单。</p>
<ul>
<li>报价回报</li>
</ul>
<p>指报价的状态回报，有未知单报价回报、未成交报价回报、全部成交报价回报。对应回调函数OnRtnQuote，以QuoteStatus字段区分。</p>
<ul>
<li>报单回报</li>
</ul>
<p>指报单的状态回报，有未知单报单回报、未成交报单回报、部分成交报单回报、全部成交报单回报和撤单回报。对应回调函数OnRtnOrder，以OrderStatus字段区分。</p>
<ul>
<li>成交回报</li>
</ul>
<p>指报单成交后推送的成交回报，对应回调函数OnRtnTrade。</p>
<span class="anchor" id="e9c48f5a-b3a1-4aa9-a564-0f03dce10f91"></span>
## 2.回调规则
<p>测试场景1</p>
<p>CZCE做市商报价，报价合约SR911P4100，开仓，买报价100，卖报价150，买数量1手，卖数量1手，先买成交1手，后又卖成交1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报价</p>
<p>ReqQuoteInsert</p>
<p>OnRtnOrder（未知单-卖）</p>
<p>OnRtnOrder（未知单-买）</p>
<p>OnRtnQuote（未知单）</p>
<p>此时CTP接收到交易所未成交报价回报和报单回报。</p>
<p>OnRtnQuote（未成交）</p>
<p>OnRtnOrder（未成交-买）</p>
<p>OnRtnOrder（未成交-卖）</p>
<p>此时CTP接收到交易所买方向全部成交的成交回报和报单回报。</p>
<p>OnRtnOrder（全部成交-买）</p>
<p>OnRtnTrade（买）</p>
<p>此时CTP接收到交易所卖方向的全部成交成交回报和报单回报，以及全部成交报价回报。</p>
<p>OnRtnQuote（全部成交）</p>
<p>OnRtnOrder（全部成交-卖）</p>
<p>OnRtnTrade（卖）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<blockquote>
<p>注意：报价的衍生单（报价两条单腿报单）的回报顺序取决于交易所返回的衍生单的回报顺序。例如测试场景1中，交易所先推送买未成交报单回报后推送卖未成交回报，则CTP也会照此顺序推送。成交回报同理，因此对于报价及衍生单的买卖回报顺序是不固定的。</p>
</blockquote>
<p>测试场景2</p>
<p>DCE做市商报价，报价合约m1911-C-2400，开仓，买报价400，卖报价500，买数量1手，卖数量1手，买成交1手，卖成交1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报价</p>
<p>ReqQuoteInsert</p>
<p>OnRtnOrder（未知单-卖）</p>
<p>OnRtnOrder（未知单-买）</p>
<p>OnRtnQuote（未知单）</p>
<p>此时CTP接收到交易所未成交报价回报和报单回报。</p>
<p>OnRtnQuote（未成交）</p>
<p>OnRtnOrder（未成交-卖）</p>
<p>OnRtnOrder（未成交-买）</p>
<p>此时CTP接收到交易所买方向全部成交的成交回报和报单回报。</p>
<p>OnRtnOrder（全部成交-卖）</p>
<p>OnRtnTrade（卖）</p>
<p>此时CTP接收到交易所卖方向的全部成交成交回报和报单回报。</p>
<p>OnRtnOrder（全部成交-买）</p>
<p>OnRtnTrade（买）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<blockquote>
<p>注意：DCE区别于其他交易所，其报价状态只推送一次，即使后续状态发生变化，也不再推送。因此测试场景2相比场景1，会少一笔状态为全部成交的报价回报。</p>
</blockquote>
<p>测试场景3</p>
<p>CZCE做市商报价撤单，报价合约CF001C12200，开仓，买报价2199，卖报价3369，买数量1手，卖数量1手，撤报价。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报价</p>
<p>ReqQuoteInsert</p>
<p>OnRtnOrder  （未知单—卖）</p>
<p>OnRtnOrder  （未知单—买）</p>
<p>OnRtnQuote  （未知单）</p>
<p>此时CTP接收到交易所未成交报价回报和报单回报。</p>
<p>OnRtnOrder  （未成交—买）</p>
<p>OnRtnOrder  （未成交—卖）</p>
<p>OnRtnQuote  （未成交）</p>
<p>此时撤报价</p>
<p>此时CTP接收到交易所已撤单报价回报和报单回报。</p>
<p>OnRtnQuote  （已撤单）</p>
<p>OnRtnOrder  （已撤单—卖）</p>
<p>OnRtnOrder  （已撤单—买）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>测试场景4</p>
<p>DCE做市商报价，撤单腿报价。报价合约c1909-C-1660，开仓，买报价179，卖报价371，买数量1手，卖数量1手；撤买单腿1手，撤卖单腿1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报价</p>
<p>ReqQuoteInsert</p>
<p>OnRtnOrder  （未知单—卖）</p>
<p>OnRtnOrder  （未知单—买）</p>
<p>OnRtnQuote  （未知单）</p>
<p>此时CTP接收到交易所未成交报价回报和报单回报。</p>
<p>OnRtnQuote  （未成交）</p>
<p>OnRtnOrder  （未成交—卖）</p>
<p>OnRtnOrder  （未成交—买）</p>
<p>此时撤单腿操作</p>
<p>OnRtnOrder  （未成交—买）</p>
<p>OnRtnOrder  （已撤单—买）</p>
<p>OnRtnOrder  （未成交—卖）</p>
<p>OnRtnOrder  （已撤单—卖）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>测试场景5</p>
<p>CZCE做市商报价，撤单腿报价，报价合约CF001C12200，开仓，买报价2199，卖报价3369，买数量1手，卖数量1手，撤买单腿1手，撤卖单腿1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报价</p>
<p>ReqQuoteInsert</p>
<p>OnRtnOrder  （未知单—卖）</p>
<p>OnRtnOrder  （未知单—买）</p>
<p>OnRtnQuote  （未知单）</p>
<p>此时CTP接收到交易所未成交报价回报和报单回报。</p>
<p>OnRtnQuote  （未成交）</p>
<p>OnRtnOrder  （未成交—买）</p>
<p>OnRtnOrder  （未成交—卖）</p>
<p>此时撤买单腿</p>
<p>此时CTP接收到交易所买撤单报单回报和错单回报。</p>
<p>OnRtnOrder  （未成交—买）</p>
<p>OnErrRtnOrderAction  [CZCE:出错: 所撤委托单没有找到]</p>
<p>此时撤卖单腿</p>
<p>此时CTP接收到交易所买撤单报单回报和错单回报。</p>
<p>OnRtnOrder  （未成交—卖）</p>
<p>OnErrRtnOrderAction  [CZCE:出错: 所撤委托单没有找到]</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<blockquote>
<p>郑商所和上期所报价只支持撤报价，不支持撤单腿，因此报错。</p>
</blockquote>
<p>测试场景6</p>
<p>CZCE做市商报价。报价合约CF001C13000，开仓，买报价1700，卖报价2800，买数量1手，卖数量1手；再报价，报价合约仍是CF001C13000，开仓。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>第一次报价</p>
<p>ReqQuoteInsert</p>
<p>OnRtnOrder  （未知单—卖）</p>
<p>OnRtnOrder  （未知单—买）</p>
<p>OnRtnQuote  （未知单）</p>
<p>此时CTP接收到交易所未成交报价回报和报单回报。</p>
<p>OnRtnQuote  （未成交）</p>
<p>OnRtnOrder  （未成交—买）</p>
<p>OnRtnOrder  （未成交—卖）</p>
<p>第二次报价（郑商所的第二次报价会自动撤销第一次报价）</p>
<p>ReqQuoteInsert</p>
<p>OnRtnOrder  （未知单—卖）</p>
<p>OnRtnOrder  （未知单—买）</p>
<p>OnRtnQuote  （未知单）</p>
<p>此时CTP接收到交易所如下回报：第一次报价的已撤单报价回报和报单回报，第二次报价的未成交报价回报和报单回报。</p>
<p>OnRtnQuote  （已撤销，第一次报价）</p>
<p>OnRtnOrder  （已撤单—买，第一次报价）</p>
<p>OnRtnOrder  （已撤单—卖，第一次报价）</p>
<p>OnRtnQuote  （未成交，第二次报价）</p>
<p>OnRtnOrder  （未成交—买，第二次报价）</p>
<p>OnRtnOrder  （未成交—卖，第二次报价）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<blockquote>
<p>郑商所的第二次报价会自动撤销第一次报价。</p>
</blockquote>
<p>测试场景7</p>
<p>DCE做市商报价，撤报价。报价合约m1707-C-2700，开仓，买报价63，卖报价349，买数量1手，卖数量1手；撤报价1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报价</p>
<p>ReqQuoteInsert</p>
<p>OnRtnOrder  （未知单—卖）</p>
<p>OnRtnOrder  （未知单—买）</p>
<p>OnRtnQuote  （未知单）</p>
<p>此时CTP接收到交易所未成交报价回报和报单回报。</p>
<p>OnRtnQuote  （未成交）</p>
<p>OnRtnOrder  （未成交—卖）</p>
<p>OnRtnOrder  （未成交—买）</p>
<p>此时撤报价操作</p>
<p>OnRtnOrder  （未成交—卖）</p>
<p>OnRtnOrder  （未成交—买）</p>
<p>OnRtnQuote  （未成交）</p>
<p>OnRtnOrder  （已撤单—卖）</p>
<p>OnRtnOrder  （已撤单—买）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<blockquote>
<p>大商所报价后，交易所推送报价响应（未成交），此时撤报价，返回两腿的报单回报（已撤单），但是报价状态不会再推送</p>
</blockquote>
