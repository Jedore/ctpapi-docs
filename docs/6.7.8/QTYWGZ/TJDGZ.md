<span class="anchor" id="0d3d2d7b-b0eb-4d88-9ad5-e38944cf8919"></span>
## 1.简介
<p>条件单是一个带有触发条件的指令。该触发条件可以以市场上的最新行情为基准，也可以以指定价格为基准。比如：一个投资者有1手IF1910的空头持仓，并希望在市场价低于2200时买入平仓，他就可以使用条件单。这样当行情波动到满足该条件时，该报单就会被自动触发报出，而不需要他本人时刻盯着电脑屏幕去监视市场行情。</p>
<p>申报条件单时，条件单的报单回报中OrderSysID是以字符串“TJBD_”开头的由CTP系统自定义的报单编号，针对该交易所当日唯一；只对成功申报的条件单编号，错单不编号。因为这种情况下的编号由CTP系统自行维护，与交易所无关，仅用于管理本系统内的该条件单。</p>
<p>有效的使用条件单，可以做出限价止损指令（stop-and-limit order）和触及市价指令（market-if-touched order）。</p>
<p>CTP条件单为CTP后台系统自带指令，并非交易所官方支持指令。</p>
<span class="anchor" id="736606c0-2b66-4675-95bc-883dfc6694ab"></span>
## 2.指令介绍
<p>报入条件单指令使用<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>函数</p>
<p>其中的核心数据结构是CThostFtdcInputOrderField</p>
<p>在结构体中和普通报单有区别的字段如下：</p>
<pre><code>    ///触发条件
    TThostFtdcContingentConditionType   ContingentCondition;
    ///止损价
    TThostFtdcPriceType StopPrice;
</code></pre>
<p>条件单有效的触发条件如下：</p>
<pre><code>    ///最新价大于条件价
    #define THOST_FTDC_CC_LastPriceGreaterThanStopPrice '5'
    ///最新价大于等于条件价
    #define THOST_FTDC_CC_LastPriceGreaterEqualStopPrice '6'
    ///最新价小于条件价
    #define THOST_FTDC_CC_LastPriceLesserThanStopPrice '7'
    ///最新价小于等于条件价
    #define THOST_FTDC_CC_LastPriceLesserEqualStopPrice '8'
    ///卖一价大于条件价
    #define THOST_FTDC_CC_AskPriceGreaterThanStopPrice '9'
    ///卖一价大于等于条件价
    #define THOST_FTDC_CC_AskPriceGreaterEqualStopPrice 'A'
    ///卖一价小于条件价
    #define THOST_FTDC_CC_AskPriceLesserThanStopPrice 'B'
    ///卖一价小于等于条件价
    #define THOST_FTDC_CC_AskPriceLesserEqualStopPrice 'C'
    ///买一价大于条件价
    #define THOST_FTDC_CC_BidPriceGreaterThanStopPrice 'D'
    ///买一价大于等于条件价
    #define THOST_FTDC_CC_BidPriceGreaterEqualStopPrice 'E'
    ///买一价小于条件价
    #define THOST_FTDC_CC_BidPriceLesserThanStopPrice 'F'
    ///买一价小于等于条件价
    #define THOST_FTDC_CC_BidPriceLesserEqualStopPrice 'H'
</code></pre>
<p>条件价对应的字段为StopPrice</p>
<span class="anchor" id="34734365-16a4-4aa3-90b9-0a1431758f2c"></span>
## 3.条件单回调规则
<ul>
<li>测试场景一</li>
</ul>
<p>报入一笔中金所条件单，触发后类型为限价单，报入后未成交。</p>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>Direction [0] 买卖方向：买</p>
<p>ExchangeID [CFFEX]</p>
<p>CurrencyID [CNY]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]</p>
<p>IsAutoSuspend [0]</p>
<p>ForceCloseReason [0]  强平原因：非强平</p>
<p>ContingentCondition [H]   <strong><font color="#FF0000">触发条件：买一价小于等于条件价</font></strong></p>
<p>StopPrice [50000]      <strong><font color="#FF0000">条件价</font></strong></p>
<p>OrderPriceType [2]    <strong><font color="#FF0000">触发后的报单价格条件：限价</font></strong></p>
<p>LimitPrice [5246] <strong><font color="#FF0000">触发后的委托价</font></strong></p>
<p>TimeCondition [3] <strong><font color="#FF0000">触发后的有效期类型：当日有效</font></strong></p>
<p>VolumeCondition [1]   <strong><font color="#FF0000">触发后的成交量类型：任何数量</font></strong></p>
</blockquote>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报入后，此时收到报单回报：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [b]  尚未触发）  </p>
<p>当触发条件满足时，收到报单回报：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [c]  已触发）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [a]  未知，报单已提交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [3]  未成交还在队列中）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景二</li>
</ul>
<p>报入一笔中金所条件单，触发后类型为限价单，报入并触发后被CTP拒绝。</p>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>Direction [0] 买卖方向：买</p>
<p>ExchangeID [CFFEX]</p>
<p>CurrencyID [CNY]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]</p>
<p>IsAutoSuspend [0]</p>
<p>ForceCloseReason [0]  强平原因：非强平</p>
<p>ContingentCondition [H]   <strong><font color="#FF0000">触发条件：买一价小于等于条件价</font></strong></p>
<p>StopPrice [50000]      <strong><font color="#FF0000">条件价</font></strong></p>
<p>OrderPriceType [2]    <strong><font color="#FF0000">触发后的报单价格条件：限价</font></strong></p>
<p>LimitPrice [5246] <strong><font color="#FF0000">触发后的委托价</font></strong></p>
<p>TimeCondition [3] <strong><font color="#FF0000">触发后的有效期类型：当日有效</font></strong></p>
<p>VolumeCondition [1]   <strong><font color="#FF0000">触发后的成交量类型：任何数量</font></strong></p>
</blockquote>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报入后，此时收到报单回报：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [b]  尚未触发）  </p>
<p>当触发条件满足时，收到报单回报及CTP返回的报错：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [c]  已触发）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNERRORCONDITIONALORDER/">OnRtnErrorConditionalOrder</a>（ErrorMsg [CTP:资金不足]）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<p>注意：<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNERRORCONDITIONALORDER/">OnRtnErrorConditionalOrder</a>为私有流回报，可用私有流重传模式RESTART重新收取该回报。</p>
<ul>
<li>测试场景三</li>
</ul>
<p>报入一笔中金所条件单，触发后类型为限价单，报入并触发后被交易所拒绝。</p>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>Direction [0] 买卖方向：买</p>
<p>ExchangeID [CFFEX]</p>
<p>CurrencyID [CNY]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]</p>
<p>IsAutoSuspend [0]</p>
<p>ForceCloseReason [0]  强平原因：非强平</p>
<p>ContingentCondition [H]   <strong><font color="#FF0000">触发条件：买一价小于等于条件价</font></strong></p>
<p>StopPrice [50000]      <strong><font color="#FF0000">条件价</font></strong></p>
<p>OrderPriceType [2]    <strong><font color="#FF0000">触发后的报单价格条件：限价</font></strong></p>
<p>LimitPrice [25600] <strong><font color="#FF0000">触发后的委托价</font></strong></p>
<p>TimeCondition [3] <strong><font color="#FF0000">触发后的有效期类型：当日有效</font></strong></p>
<p>VolumeCondition [1]   <strong><font color="#FF0000">触发后的成交量类型：任何数量</font></strong></p>
</blockquote>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报入后，此时收到报单回报：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [b]  尚未触发）  </p>
<p>当触发条件满足时，收到报单回报及交易所返回的报错：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [c]  已触发）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [a]  未知，报单已提交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [5] 已撤单报单被拒绝CFFEX:超出当时价格保护带上带价格）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景四</li>
</ul>
<p>报入一笔中金所条件单，触发后类型为FOK，报入后未成交自动被撤销。</p>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>Direction [0] 买卖方向：买</p>
<p>ExchangeID [CFFEX]</p>
<p>CurrencyID [CNY]</p>
<p>VolumeTotalOriginal [8]   报单手数：1手</p>
<p>MinVolume [8]</p>
<p>IsSwapOrder [0]</p>
<p>IsAutoSuspend [0]</p>
<p>ForceCloseReason [0]  强平原因：非强平</p>
<p>ContingentCondition [H]   <strong><font color="#FF0000">触发条件：买一价小于等于条件价</font></strong></p>
<p>StopPrice [50000]      <strong><font color="#FF0000">条件价</font></strong></p>
<p>OrderPriceType [2]    <strong><font color="#FF0000">触发后的报单价格条件：限价</font></strong></p>
<p>LimitPrice [5246] <strong><font color="#FF0000">触发后的委托价</font></strong></p>
<p>TimeCondition [1] <strong><font color="#FF0000">触发后的有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [3]   <strong><font color="#FF0000">触发后的成交量类型：全部数量</font></strong></p>
</blockquote>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报入后，此时收到报单回报：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [b]  尚未触发）  </p>
<p>当触发条件满足时，收到报单回报及交易所返回的报错：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [c]  已触发）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [a]  未知，报单已提交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [5] 已撤单报单已提交）</p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
<ul>
<li>测试场景五</li>
</ul>
<p>报入一笔中金所条件单，触发后类型为FAK，报入后部成部撤。</p>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>Direction [0] 买卖方向：买</p>
<p>ExchangeID [CFFEX]</p>
<p>CurrencyID [CNY]</p>
<p>VolumeTotalOriginal [8]   报单手数：1手</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]</p>
<p>IsAutoSuspend [0]</p>
<p>ForceCloseReason [0]  强平原因：非强平</p>
<p>ContingentCondition [H]   <strong><font color="#FF0000">触发条件：买一价小于等于条件价</font></strong></p>
<p>StopPrice [50000]      <strong><font color="#FF0000">条件价</font></strong></p>
<p>OrderPriceType [2]    <strong><font color="#FF0000">触发后的报单价格条件：限价</font></strong></p>
<p>LimitPrice [5246] <strong><font color="#FF0000">触发后的委托价</font></strong></p>
<p>TimeCondition [1] <strong><font color="#FF0000">触发后的有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [2]   <strong><font color="#FF0000">触发后的成交量类型：最小数量</font></strong></p>
</blockquote>
<table border="0" cellspacing="0" class="square-block" id=""><tbody border="0"><tr border="0"><td class="square-block-left"></td><td class="square-block-content"><div>
<p>报入后，此时收到报单回报：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [b]  尚未触发）  </p>
<p>当触发条件满足时，收到报单回报及交易所返回的报错：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [c]  已触发）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [a]  未知，报单已提交）</p>
<p>此时CTP收到了交易所推送的撤单状态的报单回报：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [5] 已撤单报单已提交）</p>
<p>此时CTP收到了交易所推送的成交回报：</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNORDER/">OnRtnOrder</a>（OrderStatus [5] 已撤单报单已提交）</p>
<p><a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNTRADE/">OnRtnTrade</a></p>
</div></td><td class="square-block-right"></td></tr></tbody></table>
