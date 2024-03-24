<p>深度行情通知，当SubscribeMarketData订阅行情后，行情通知由此推送。</p>
<span class="anchor" id="d6c922f3-cf89-400a-b631-f834283f9b8b"></span>
## 1.函数原型
<p>virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {};</p>
<span class="anchor" id="3c1c61bf-a62c-4774-ba83-c873a025d397"></span>
## 2.参数
<p>pDepthMarketData：深度行情</p>
<pre><code>struct CThostFtdcDepthMarketDataField
{
    ///交易日
    TThostFtdcDateType   TradingDay;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType    ExchangeInstID;
    ///最新价
    TThostFtdcPriceType  LastPrice;
    ///上次结算价
    TThostFtdcPriceType  PreSettlementPrice;
    ///昨收盘
    TThostFtdcPriceType  PreClosePrice;
    ///昨持仓量
    TThostFtdcLargeVolumeType   PreOpenInterest;
    ///今开盘
    TThostFtdcPriceType  OpenPrice;
    ///最高价
    TThostFtdcPriceType  HighestPrice;
    ///最低价
    TThostFtdcPriceType  LowestPrice;
    ///数量
    TThostFtdcVolumeType Volume;
    ///成交金额
    TThostFtdcMoneyType  Turnover;
    ///持仓量
    TThostFtdcLargeVolumeType   OpenInterest;
    ///今收盘
    TThostFtdcPriceType  ClosePrice;
    ///本次结算价
    TThostFtdcPriceType  SettlementPrice;
    ///涨停板价
    TThostFtdcPriceType  UpperLimitPrice;
    ///跌停板价
    TThostFtdcPriceType  LowerLimitPrice;
    ///昨虚实度
    TThostFtdcRatioType  PreDelta;
    ///今虚实度
    TThostFtdcRatioType  CurrDelta;
    ///最后修改时间
    TThostFtdcTimeType   UpdateTime;
    ///最后修改毫秒
    TThostFtdcMillisecType   UpdateMillisec;
    ///申买价一
    TThostFtdcPriceType  BidPrice1;
    ///申买量一
    TThostFtdcVolumeType BidVolume1;
    ///申卖价一
    TThostFtdcPriceType  AskPrice1;
    ///申卖量一
    TThostFtdcVolumeType AskVolume1;
    ///申买价二
    TThostFtdcPriceType  BidPrice2;
    ///申买量二
    TThostFtdcVolumeType BidVolume2;
    ///申卖价二
    TThostFtdcPriceType  AskPrice2;
    ///申卖量二
    TThostFtdcVolumeType AskVolume2;
    ///申买价三
    TThostFtdcPriceType  BidPrice3;
    ///申买量三
    TThostFtdcVolumeType BidVolume3;
    ///申卖价三
    TThostFtdcPriceType  AskPrice3;
    ///申卖量三
    TThostFtdcVolumeType AskVolume3;
    ///申买价四
    TThostFtdcPriceType  BidPrice4;
    ///申买量四
    TThostFtdcVolumeType BidVolume4;
    ///申卖价四
    TThostFtdcPriceType  AskPrice4;
    ///申卖量四
    TThostFtdcVolumeType AskVolume4;
    ///申买价五
    TThostFtdcPriceType  BidPrice5;
    ///申买量五
    TThostFtdcVolumeType BidVolume5;
    ///申卖价五
    TThostFtdcPriceType  AskPrice5;
    ///申卖量五
    TThostFtdcVolumeType AskVolume5;
    ///当日均价
    TThostFtdcPriceType  AveragePrice;
    ///业务日期
    TThostFtdcDateType   ActionDay;
};
</code></pre>
<span class="anchor" id="5aeafaad-8f53-4a40-8562-6e23716d9aef"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="910f7051-476e-4081-aa6f-c3c48b6fc7bc"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">行情中有些字段出现极大值，为什么？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>行情通知中，例如结算价、收盘价、买卖价出现double极大值，则表示该字段没有值。例如涨停板的时候，因为没有卖价，会给出一个double极大值，同时卖量为0。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">郑商所的结算价在盘中也会送出，但数值在盘中不会变化，这和盘后推送的结算价怎么区分？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>郑商所夜盘收盘后会推送结算价，这也就是早上行情中有可能会收到结算价的原因，盘中行情中推送的结算价数值不会发生变化。无夜盘的合约，盘中不会收到结算价。白盘收盘后郑商所也会推送所有合约最新的结算价，CTP对交易所推送的结算价不做处理，直接转发。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">郑商所的UDP行情里，Tradingday和AveragePrice字段都是空的，但是TCP行情里有，这是为什么？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>UDP行情不推送AveragePrice字段；TCP行情里的Tradingday和AveragePrice是CTP给的。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_4" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">行情中哪些字段是CTP自己计算发出的？</p><div class="region_panel" id="region_panel_4" style="display:block;"><table><tr><td>
<p>郑商所的套利合约的涨跌停板价由CTP计算，交易所不发</p>
<p>成交总额郑商所不推送由CTP计算，另外cffex,dce,shfe,ine这几家的成交均价不推送，由ctp计算。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_4" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_5" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">发现连上前置后，为什么收到的行情涨跌停价是0？</p><div class="region_panel" id="region_panel_5" style="display:block;"><table><tr><td>
<p>连上的如果是mdfront的话可能mdfront是级联的，也就是说上一级还是mdfront这两个mdfront如果版本不对，也同样会导致这个问题</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_5" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_6" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">订阅后大商所组合合约行情不跳动，其他交易终端（闪电王、快期等）的组合合约都有行情且在跳跃，为什么？</p><div class="region_panel" id="region_panel_6" style="display:block;"><table><tr><td>
<p>大商所只会推送单腿合约的行情，组合合约的行情需要下端自行计算。其他终端则是实时计算两条腿的价差，故行情看上去一直跳跃。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_6" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
