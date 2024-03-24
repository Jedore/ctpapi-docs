<p>由于各家交易所的报单指令略有不同，故在此列出各家交易所报单接口情况。</p>
<span class="anchor" id="73161633-1c27-41d8-8b62-d2d2f7a72a68"></span>
## 1.各交易所指令
<span class="anchor" id="d103a767-0d02-48d0-b433-1221f305adcd"></span>
### 1.1.上期所
<ul>
<li>1.上期所立即单FOK</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [SHFE]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] <strong><font color="#FF0000">有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [3]   <strong><font color="#FF0000">成交量类型：全部数量</font></strong></p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>ForceCloseReason [0]  强平原因：非强平</p>
</blockquote>
<ul>
<li>2.上期所立即单FAK</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [SHFE]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] <strong><font color="#FF0000">有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [2]   <strong><font color="#FF0000">成交量类型：最小数量</font></strong></p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>ForceCloseReason [0]</p>
</blockquote>
<span class="anchor" id="eead9a06-3a4b-4320-942f-7e11cf36bad7"></span>
### 1.2.大商所
<ul>
<li>1.大商所立即单FOK</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [DCE]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1] 最小成交量：1手</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] <strong><font color="#FF0000">有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [3]   <strong><font color="#FF0000">成交量类型：全部数量</font></strong></p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>2.大商所立即单FAK</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [DCE]</p>
<p>VolumeTotalOriginal [3]   报单手数：3手</p>
<p>MinVolume [1] 最小成交量：1手</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] <strong><font color="#FF0000">有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [2]   <strong><font color="#FF0000">成交量类型：最小数量</font></strong></p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>3.大商所市价单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [DCE]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1] 最小成交量：1手</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [1]    <strong><font color="#FF0000">报单价格条件：任意价</font></strong></p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] <strong><font color="#FF0000">有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [3]   成交量类型：全部数量</p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>LimitPrice [0.00000000]   <strong><font color="#FF0000">价格：0</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>4.大商所止盈单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [DCE]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1] 最小成交量：1手</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] <strong><font color="#FF0000">有效期类型：当日有效</font></strong></p>
<p>VolumeCondition [1]   成交量类型：任何数量</p>
<p>ContingentCondition [3]   <strong><font color="#FF0000">触发条件：止盈</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>5.大商所止损单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [DCE]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1] 最小成交量：1手</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] <strong><font color="#FF0000">有效期类型：当日有效</font></strong></p>
<p>VolumeCondition [1]   成交量类型：任何数量</p>
<p>ContingentCondition [2]   <strong><font color="#FF0000">触发条件：止损</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>6.大商所市价止盈单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [DCE]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1] 最小成交量：1手</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [1]    <strong><font color="#FF0000">报单价格条件：任意价</font></strong></p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] <strong><font color="#FF0000">有效期类型：当日有效</font></strong></p>
<p>VolumeCondition [1]   成交量类型：任何数量</p>
<p>ContingentCondition [3]   <strong><font color="#FF0000">触发条件：止盈</font></strong></p>
<p>LimitPrice [0.00000000]   <strong><font color="#FF0000">价格：0</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>7.大商所市价止损单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [DCE]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1] 最小成交量：1手</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [1]    <strong><font color="#FF0000">报单价格条件：任意价</font></strong></p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] <strong><font color="#FF0000">有效期类型：当日有效</font></strong></p>
<p>VolumeCondition [1]   成交量类型：任何数量</p>
<p>ContingentCondition [2]   <strong><font color="#FF0000">触发条件：止损</font></strong></p>
<p>LimitPrice [0.00000000]   <strong><font color="#FF0000">价格：0</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>8.大商所互换单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [1]    组合开平标注：平仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [DCE]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1] 最小成交量：1手</p>
<p>IsSwapOrder [1]   <strong><font color="#FF0000">互换单标志：是</font></strong></p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [1] 买卖方向：卖</p>
<p>TimeCondition [3] 有效期类型：当日有效</p>
<p>VolumeCondition [2]   成交量类型：最小数量</p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>9.大商所套利单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>InstrumentID [SP a2109&amp;a2201] <strong><font color="#FF0000">合约填套利合约</font></strong></p>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [DCE]</p>
<p>VolumeTotalOriginal [1]   报单手数：1手</p>
<p>MinVolume [1] 最小成交量：1手</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] 有效期类型：当日有效</p>
<p>VolumeCondition [2]   成交量类型：最小数量</p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>10.大商所申请组合</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQCOMBACTIONINSERT/">ReqCombActionInsert</a></p>
<blockquote>
<p><reqcombactioninsert></reqcombactioninsert></p>
<p>BrokerID [1008]</p>
<p>InvestorID [90096650]</p>
<p>InstrumentID [OPL m2109-C-2800&amp;m2109-C-2800]</p>
<p>CombActionRef []</p>
<p>UserID [90096650]</p>
<p>ExchangeID [DCE]</p>
<p>IPAddress []</p>
<p>MacAddress []</p>
<p>InvestUnitID []</p>
<p>Volume [1]</p>
<p>FrontID [0]</p>
<p>SessionID [0]</p>
<p>Direction [0] 买卖方向：买</p>
<p>CombDirection [0] <strong><font color="#FF0000">组合指令方向：申请组合</font></strong></p>
<p>HedgeFlag [1] 投机套保标志：投机</p>
<p>nRequestID [1]</p>
<p></p>
</blockquote>
<span class="anchor" id="16bd8b51-09e1-4310-b250-8f14d331ad26"></span>
### 1.3.中金所
<ul>
<li>1.中金所立即单FOK</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CFFEX]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]   互换单标志：否</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] <strong><font color="#FF0000">有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [3]   <strong><font color="#FF0000">成交量类型：全部数量</font></strong></p>
<p>ContingentCondition [1]   <strong><font color="#FF0000">触发条件：立即触发</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>2.中金所立即单FAK</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CFFEX]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]   互换单标志：否</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] <strong><font color="#FF0000">有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [2]   <strong><font color="#FF0000">成交量类型：最小数量</font></strong></p>
<p>ContingentCondition [1]   <strong><font color="#FF0000">触发条件：立即触发</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>3.中金所市价单-最优价</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CFFEX]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]   互换单标志：否</p>
<p>OrderPriceType [3]    <strong><font color="#FF0000">报单价格条件：最优价</font></strong></p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] 有效期类型：立即完成，否则撤销</p>
<p>VolumeCondition [1]   <strong><font color="#FF0000">成交量类型：任何数量</font></strong></p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>LimitPrice [0.00000000]   <strong><font color="#FF0000">价格：0</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>4.中金所市价单-最优价转限价</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CFFEX]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]   互换单标志：否</p>
<p>OrderPriceType [3]    <strong><font color="#FF0000">报单价格条件：最优价</font></strong></p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] <strong><font color="#FF0000">有效期类型：当日有效</font></strong></p>
<p>VolumeCondition [1]   <strong><font color="#FF0000">成交量类型：任何数量</font></strong></p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>LimitPrice [0.00000000]   <strong><font color="#FF0000">价格：0</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<p><span alt="" id="anchor-id-04"></span> </p>
<ul>
<li>5.中金所市价单-五档价</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CFFEX]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]   互换单标志：否</p>
<p>OrderPriceType [G]    <strong><font color="#FF0000">报单价格条件：五档价</font></strong></p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] 有效期类型：立即完成，否则撤销</p>
<p>VolumeCondition [1]   <strong><font color="#FF0000">成交量类型：任何数量</font></strong></p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>LimitPrice [0.00000000]   <strong><font color="#FF0000">价格：0</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>6.中金所市价单-五档价转限价</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CFFEX]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]   互换单标志：否</p>
<p>OrderPriceType [G]    <strong><font color="#FF0000">报单价格条件：五档价</font></strong></p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] <strong><font color="#FF0000">有效期类型：当日有效</font></strong></p>
<p>VolumeCondition [1]   <strong><font color="#FF0000">成交量类型：任何数量</font></strong></p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>LimitPrice [0.00000000]   <strong><font color="#FF0000">价格：0</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>7.中金所套利单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [2] <strong><font color="#FF0000">组合投机套保标志：套利</font></strong></p>
<p>ExchangeID [CFFEX]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] 有效期类型：当日有效</p>
<p>VolumeCondition [2]   成交量类型：最小数量</p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>ForceCloseReason [0]</p>
</blockquote>
<span class="anchor" id="66a04d08-f596-4b06-ab1d-b9da5029c1b4"></span>
### 1.4.郑商所
<ul>
<li>1.郑商所立即单FOK</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CZCE]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] <strong><font color="#FF0000">有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [3]   <strong><font color="#FF0000">成交量类型：全部数量</font></strong></p>
<p>ContingentCondition [1]   <strong><font color="#FF0000">触发条件：立即触发</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>2.郑商所立即单FAK</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CZCE]</p>
<p>VolumeTotalOriginal [3]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [1] <strong><font color="#FF0000">有效期类型：立即完成，否则撤销</font></strong></p>
<p>VolumeCondition [2]   <strong><font color="#FF0000">成交量类型：最小数量</font></strong></p>
<p>ContingentCondition [1]   <strong><font color="#FF0000">触发条件：立即触发</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>3.郑商所市价单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CZCE]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]</p>
<p>OrderPriceType [1]    <strong><font color="#FF0000">报单价格条件：任意价</font></strong></p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] 有效期类型：当日有效</p>
<p>VolumeCondition [3]   成交量类型：全部数量</p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>LimitPrice [0.00000000]   <strong><font color="#FF0000">价格：0</font></strong></p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>4.郑商所套利单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>InstrumentID [SPD TA109&amp;TA110]    <strong><font color="#FF0000">合约填套利合约</font></strong></p>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CZCE]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]   互换单标志：否</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] 有效期类型：当日有效</p>
<p>VolumeCondition [2]   成交量类型：最小数量</p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>5.郑商所互换单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a></p>
<blockquote>
<p>CombOffsetFlag [1]    组合开平标注：平仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CZCE]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [1]   <strong><font color="#FF0000">互换单标志：是</font></strong></p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [1] 买卖方向：卖</p>
<p>TimeCondition [3] 有效期类型：当日有效</p>
<p>VolumeCondition [2]   成交量类型：最小数量</p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>ForceCloseReason [0]</p>
</blockquote>
<ul>
<li>6.郑商所组合单</li>
</ul>
<p>调用接口：<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQCOMBACTIONINSERT/">ReqCombActionInsert</a></p>
<blockquote>
<p>InstrumentID [SPD TA109&amp;TA206]    <strong><font color="#FF0000">填组合合约</font></strong></p>
<p>CombOffsetFlag [0]    组合开平标注：开仓</p>
<p>CombHedgeFlag [1] 组合投机套保标志：投机</p>
<p>ExchangeID [CZCE]</p>
<p>VolumeTotalOriginal [1]</p>
<p>MinVolume [1]</p>
<p>IsSwapOrder [0]   互换单标志：否</p>
<p>OrderPriceType [2]    报单价格条件：限价</p>
<p>Direction [0] 买卖方向：买</p>
<p>TimeCondition [3] 有效期类型：当日有效</p>
<p>VolumeCondition [2]   成交量类型：最小数量</p>
<p>ContingentCondition [1]   触发条件：立即触发</p>
<p>ForceCloseReason [0]</p>
</blockquote>
<span class="anchor" id="fd6ad3d3-9b2e-4f89-8e8d-c28ba51dbce0"></span>
### 1.5.广期所
<p>报单指令同大商所，请参考大商所</p>
