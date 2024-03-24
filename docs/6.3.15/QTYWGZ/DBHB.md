<p>本文例举了一些常用的报单操作所对应的回调规则。在给定交易所报单回报顺序的前提下，CTP返回给API的回调顺序是固定的。</p>
<p>目前大商所的回报比较特殊，当一笔委托全部成交后，大商所直接返回该笔委托的成交回报，而不返回状态为全部成交的报单回报，对于这种情况，CTP会补一个状态为全部成交的报单回报，下文会举例说明。</p>
<span class="anchor" id="279a874b-c595-4d1b-80d9-56a527474fbd"></span>
## 1.术语说明
<ul>
<li>报单回报</li>
</ul>
<p>指报单的状态回报，有未知单报单回报、未成交报单回报、部分成交报单回报、全部成交报单回报和撤单回报。对应回调函数OnRtnOrder，以OrderStatus字段区分。</p>
<ul>
<li>成交回报</li>
</ul>
<p>指报单成交后推送的成交回报，对应回调函数OnRtnTrade。</p>
<ul>
<li>错单响应</li>
</ul>
<p>指报单被CTP拒绝后返回的响应通知，对应回调函数OnRspOrderInsert，其中ErrorID和ErrorMsg指明了错误原因。</p>
<ul>
<li>错单回报</li>
</ul>
<p>指报单被CTP或交易所拒绝后的报单的状态回报。对应回调函数OnErrRtnOrderInsert。</p>
<span class="anchor" id="aa918565-7ddd-4695-956a-9c1edf1bbb14"></span>
## 2.回调规则
<p>测试场景1</p>
<p>报单合约ag1207，报入1手，到交易所先未成交，后全部成交1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p>ReqOrderInsert</p>
<p>回调顺序：</p>
<p>OnRtnOrder （未知单） </p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p>OnRtnOrder （未成交）</p>
<p>此时CTP接收到交易所的成交回报和全部成交报单回报</p>
<p>OnRtnOrder （未成交）</p>
<p>OnRtnOrder （全部成交）</p>
<p>OnRtnTrade</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>测试场景2</p>
<p>报单合约ag1207，报入1手，到交易所立即全部成交1手。（注意，此案例没有收到交易所的未成交回报状态，而是直接收到全部成交状态）</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p>ReqOrderInsert</p>
<p>OnRtnOrder （未知单）</p>
<p>此时CTP接收到交易所的成交回报和成交报单回报</p>
<p>OnRtnOrder （未知单）</p>
<p>OnRtnOrder （全部成交报单已提交）</p>
<p>OnRtnTrade</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>测试场景3</p>
<p>报单合约ag1207，报入1手，到交易所先未成交，然后撤单1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p>ReqOrderInsert</p>
<p>OnRtnOrder（未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p>OnRtnOrder（未成交）</p>
<p>ReqOrderAction</p>
<p>此时CTP接收到交易所的撤单报单回报</p>
<p>OnRtnOrder（未成交）</p>
<p>OnRtnOrder（已撤单）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>测试场景4</p>
<p>报单合约ag1207，报入10手，到交易所先未成交，然后成交3手，然后剩余全部成交7手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p>ReqOrderInsert</p>
<p>OnRtnOrder （未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p>OnRtnOrder （未成交）</p>
<p>此时CTP接收到交易所的成交回报和部分成交报单回报</p>
<p>OnRtnOrder （未成交）</p>
<p>OnRtnOrder （部分成交）</p>
<p>OnRtnTrade</p>
<p>此时CTP接收到交易所的成交回报和全部成交报单回报</p>
<p>OnRtnOrder （部分成交）</p>
<p>OnRtnOrder （全部成交）</p>
<p>OnRtnTrade</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>测试场景5</p>
<p>报单合约ag1207，报入10手，到交易所先未成交，然后成交4手，然后剩余全部撤单6手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p>ReqOrderInsert</p>
<p>OnRtnOrder （未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p>OnRtnOrder （未成交）</p>
<p>此时CTP接收到交易所的成交回报和部分成交报单回报</p>
<p>OnRtnOrder （未成交）</p>
<p>OnRtnOrder （部分成交）</p>
<p>OnRtnTrade</p>
<p>发起撤单</p>
<p>ReqOrderAction</p>
<p>此时CTP接收到交易所的撤单回报</p>
<p>OnRtnOrder（部分成交）</p>
<p>OnRtnOrder（已撤单）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>测试场景6</p>
<p>对一笔已经撤单的委托单再次撤单。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>对一笔已撤单再次撤单</p>
<p>ReqOrderAction</p>
<p>触发撤单错误响应</p>
<p>OnRspOrderAction （CTP:报单已全成交或已撤销，不能再撤）</p>
<p>触发撤单错误回报</p>
<p>OnErrRtnOrderAction （CTP:报单已全成交或已撤销，不能再撤）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>测试场景7</p>
<p>对一笔未成交委托进行撤单，因为委托号填写错误导致撤单失败</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>撤一笔不存在的委托</p>
<p>ReqOrderAction</p>
<p>触发撤单错误响应（CTP:撤单找不到相应报单）</p>
<p>OnRspOrderAction</p>
<p>触发撤单错误回报</p>
<p>OnErrRtnOrderAction （CTP:撤单找不到相应报单）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<span class="anchor" id="f94f7e0a-b6c8-4ca3-a894-1d3697fcf517"></span>
## 3.大商所特殊回调规则
<p>目前大商所的回报比较特殊，当一笔委托全部成交后，大商所直接返回该笔委托的成交回报，而不返回状态为全部成交的报单回报，对于这种情况，CTP会补一个状态为全部成交的报单回报。</p>
<p>测试场景1</p>
<p>报单合约c1911-C-1760，报入1手，到交易所先未成交，后全部成交1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p>ReqOrderInsert</p>
<p>OnRtnOrder （未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p>OnRtnOrder （未成交）</p>
<p>此时CTP接收到交易所的成交回报</p>
<p>OnRtnOrder （全部成交）（CTP补充生成，且不重复推送前一状态）</p>
<p>OnRtnTrade</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>测试场景2</p>
<p>报单合约c1911-C-1760，报入1手，到交易所立即全部成交1手。注意，大商所不管会不会立即成交，只要委托进入报单簿后都会返回一笔未成交报单回报给到CTP。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p>ReqOrderInsert</p>
<p>OnRtnOrder （未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p>OnRtnOrder （未成交）</p>
<p>此时CTP接收到交易所的成交回报</p>
<p>OnRtnOrder （全部成交）（CTP补充生成，且不重复推送前一状态）</p>
<p>OnRtnTrade</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>测试场景3</p>
<p>报单合约c1911-C-1760，报入1手，到交易所先未成交，然后撤单1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p>ReqOrderInsert</p>
<p>OnRtnOrder （未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p>OnRtnOrder （未成交）</p>
<p>发起撤单</p>
<p>ReqOrderAction</p>
<p>此时CTP接收到交易所的撤单回报</p>
<p>OnRtnOrder （未成交）</p>
<p>OnRtnOrder （已撤单）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
