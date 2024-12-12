<p>本文例举了一些常用的报单操作所对应的回调规则。在给定交易所报单回报顺序的前提下，CTP返回给API的回调顺序是固定的。</p>
<p>目前大商所的回报比较特殊，当一笔委托全部成交后，大商所直接返回该笔委托的成交回报，而不返回状态为全部成交的报单回报，对于这种情况，CTP会补一个状态为全部成交的报单回报，下文会举例说明。</p>
<span class="anchor" id="ca659cf1-6337-4c40-a025-e11fda481392"></span>
## 1.术语说明
<ul>
<li>报单回报</li>
</ul>
<p>指报单的状态回报，有未知单报单回报、未成交报单回报、部分成交报单回报、全部成交报单回报和撤单回报。对应回调函数<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>，以OrderStatus字段区分。</p>
<ul>
<li>成交回报</li>
</ul>
<p>指报单成交后推送的成交回报，对应回调函数<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a>。</p>
<ul>
<li>错单响应</li>
</ul>
<p>指报单被CTP拒绝后返回的响应通知，对应回调函数<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPORDERINSERT/">OnRspOrderInsert</a>，其中ErrorID和ErrorMsg指明了错误原因。</p>
<ul>
<li>错单回报</li>
</ul>
<p>指报单被CTP或交易所拒绝后的报单的状态回报。对应回调函数<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNORDERINSERT/">OnErrRtnOrderInsert</a>。</p>
<span class="anchor" id="7ad0c8b3-372d-42c4-b8cf-cd043817d838"></span>
## 2.回调规则
<ul>
<li>测试场景1</li>
</ul>
<p>报单合约ag1207，报入1手，到交易所先未成交，后全部成交1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p>回调顺序：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单） </p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p>此时CTP接收到交易所的成交回报和全部成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （全部成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景2</li>
</ul>
<p>报单合约ag1207，报入1手，到交易所立即全部成交1手。（注意，此案例没有收到交易所的未成交回报状态，而是直接收到全部成交状态）</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单）</p>
<p>此时CTP接收到交易所的成交回报和成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （全部成交报单已提交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景3</li>
</ul>
<p>报单合约ag1207，报入1手，到交易所先未成交，然后撤单1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（未成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERACTION/">ReqOrderAction</a></p>
<p>此时CTP接收到交易所的撤单报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（未成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（已撤单）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景4</li>
</ul>
<p>报单合约ag1207，报入10手，到交易所先未成交，然后成交3手，然后剩余全部成交7手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p>此时CTP接收到交易所的成交回报和部分成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （部分成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
<p>此时CTP接收到交易所的成交回报和全部成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （部分成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （全部成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景5</li>
</ul>
<p>报单合约ag1207，报入10手，到交易所先未成交，然后成交4手，然后剩余全部撤单6手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p>此时CTP接收到交易所的成交回报和部分成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （部分成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
<p>发起撤单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERACTION/">ReqOrderAction</a></p>
<p>此时CTP接收到交易所的撤单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（部分成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（已撤单）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景6</li>
</ul>
<p>对一笔已经撤单的委托单再次撤单。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>对一笔已撤单再次撤单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERACTION/">ReqOrderAction</a></p>
<p>触发撤单错误响应</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPORDERACTION/">OnRspOrderAction</a> （CTP:报单已全成交或已撤销，不能再撤）</p>
<p>触发撤单错误回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNORDERACTION/">OnErrRtnOrderAction</a> （CTP:报单已全成交或已撤销，不能再撤）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景7</li>
</ul>
<p>对一笔未成交委托进行撤单，因为委托号填写错误导致撤单失败</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>撤一笔不存在的委托</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERACTION/">ReqOrderAction</a></p>
<p>触发撤单错误响应（CTP:撤单找不到相应报单）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRSPORDERACTION/">OnRspOrderAction</a></p>
<p>触发撤单错误回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONERRRTNORDERACTION/">OnErrRtnOrderAction</a> （CTP:撤单找不到相应报单）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景8</li>
</ul>
<p>报入上期所FAK单子，报入后部分成交部分撤单。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报入上期所FAK</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单）</p>
<p>此时CTP收到了交易所推送的撤单状态的报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （已撤单，回报中VolumeTraded字段此时已有值）</p>
<p>此时CTP收到了交易所推送的成交回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （已撤单）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>相同场景下，能源中心和中金所FAK的回报与上期所一致。</p>
<ul>
<li>测试场景9</li>
</ul>
<p>报入大商所FAK单子，报入后部分成交部分撤单</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报入大商所FAK</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单）</p>
<p>此时CTP收到了交易所推送的未成交状态的报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p>此时CTP收到了交易所推送的成交回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （部分成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
<p>此时CTP收到了交易所推送的撤单状态的报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （已撤单）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>相同场景下，广期所FAK的回报与大商所一致。</p>
<ul>
<li>测试场景10</li>
</ul>
<p>报入郑商所FAK单子，报入后部分成交部分撤单</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报入郑商所FAK</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单）</p>
<p>此时CTP收到了交易所推送的未成交状态的报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p>此时CTP收到了交易所推送的部分成交状态的报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （部分成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
<p>此时CTP收到了交易所推送的撤单状态的报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （已撤单）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<span class="anchor" id="96ff885d-4662-4830-8762-6a706f9cb903"></span>
## 3.大商所特殊回调规则
<p>目前大商所的回报比较特殊，当一笔委托全部成交后，大商所直接返回该笔委托的成交回报，而不返回状态为全部成交的报单回报，对于这种情况，CTP会补一个状态为全部成交的报单回报。</p>
<ul>
<li>测试场景1</li>
</ul>
<p>报单合约c1911-C-1760，报入1手，到交易所先未成交，后全部成交1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p>此时CTP接收到交易所的成交回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （全部成交）（CTP补充生成，且不重复推送前一状态）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景2</li>
</ul>
<p>报单合约c1911-C-1760，报入1手，到交易所立即全部成交1手。注意，大商所不管会不会立即成交，只要委托进入报单簿后都会返回一笔未成交报单回报给到CTP。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p>此时CTP接收到交易所的成交回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （全部成交）（CTP补充生成，且不重复推送前一状态）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景3</li>
</ul>
<p>报单合约c1911-C-1760，报入1手，到交易所先未成交，然后撤单1手。</p>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未知单）</p>
<p>此时CTP接收到交易所的未成交报单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p>发起撤单</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERACTION/">ReqOrderAction</a></p>
<p>此时CTP接收到交易所的撤单回报</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （未成交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a> （已撤单）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
