<p>请求查询行情响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYDEPTHMARKETDATA/">ReqQryDepthMarketData</a>后，该方法被调用。</p>
<span class="anchor" id="6fdf22ab-b395-44cc-9e2a-09482d2cf58a"></span>
## 1.函数原型
<p>virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="fae69082-af7a-41fb-ae90-825e0c2965de"></span>
## 2.参数
<p>pDepthMarketData：深度行情</p>
<pre><code>struct CThostFtdcDepthMarketDataField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///保留的无效字段
    TThostFtdcOldExchangeInstIDType reserve2;
    ///最新价
    TThostFtdcPriceType LastPrice;
    ///上次结算价
    TThostFtdcPriceType PreSettlementPrice;
    ///昨收盘
    TThostFtdcPriceType PreClosePrice;
    ///昨持仓量
    TThostFtdcLargeVolumeType   PreOpenInterest;
    ///今开盘
    TThostFtdcPriceType OpenPrice;
    ///最高价
    TThostFtdcPriceType HighestPrice;
    ///最低价
    TThostFtdcPriceType LowestPrice;
    ///数量
    TThostFtdcVolumeType    Volume;
    ///成交金额
    TThostFtdcMoneyType Turnover;
    ///持仓量
    TThostFtdcLargeVolumeType   OpenInterest;
    ///今收盘
    TThostFtdcPriceType ClosePrice;
    ///本次结算价
    TThostFtdcPriceType SettlementPrice;
    ///涨停板价
    TThostFtdcPriceType UpperLimitPrice;
    ///跌停板价
    TThostFtdcPriceType LowerLimitPrice;
    ///昨虚实度
    TThostFtdcRatioType PreDelta;
    ///今虚实度
    TThostFtdcRatioType CurrDelta;
    ///最后修改时间
    TThostFtdcTimeType  UpdateTime;
    ///最后修改毫秒
    TThostFtdcMillisecType  UpdateMillisec;
    ///申买价一
    TThostFtdcPriceType BidPrice1;
    ///申买量一
    TThostFtdcVolumeType    BidVolume1;
    ///申卖价一
    TThostFtdcPriceType AskPrice1;
    ///申卖量一
    TThostFtdcVolumeType    AskVolume1;
    ///申买价二
    TThostFtdcPriceType BidPrice2;
    ///申买量二
    TThostFtdcVolumeType    BidVolume2;
    ///申卖价二
    TThostFtdcPriceType AskPrice2;
    ///申卖量二
    TThostFtdcVolumeType    AskVolume2;
    ///申买价三
    TThostFtdcPriceType BidPrice3;
    ///申买量三
    TThostFtdcVolumeType    BidVolume3;
    ///申卖价三
    TThostFtdcPriceType AskPrice3;
    ///申卖量三
    TThostFtdcVolumeType    AskVolume3;
    ///申买价四
    TThostFtdcPriceType BidPrice4;
    ///申买量四
    TThostFtdcVolumeType    BidVolume4;
    ///申卖价四
    TThostFtdcPriceType AskPrice4;
    ///申卖量四
    TThostFtdcVolumeType    AskVolume4;
    ///申买价五
    TThostFtdcPriceType BidPrice5;
    ///申买量五
    TThostFtdcVolumeType    BidVolume5;
    ///申卖价五
    TThostFtdcPriceType AskPrice5;
    ///申卖量五
    TThostFtdcVolumeType    AskVolume5;
    ///当日均价
    TThostFtdcPriceType AveragePrice;
    ///业务日期
    TThostFtdcDateType  ActionDay;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType    ExchangeInstID;
    ///上带价
    TThostFtdcPriceType BandingUpperPrice;
    ///下带价
    TThostFtdcPriceType BandingLowerPrice;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>Turnover：成交金额。自6.7.2版本开始，普通行情前置front的郑商所成交金额从原来的【成交均价*成交数量】改为【成交均价*成交数量*合约乘数】，与其他交易所的算法保持一致；而组播行情前置mdfront的郑商所成交金额仍然是【成交均价*成交数量】。后者的原因是郑商所交易所端给出的行情本身没有turnover字段，需要CTP自行计算，而mdfront是独立组件，只从交易所接收行情数据，不接收交易数据，无法从交易获取合约乘数，因此mdfront给出的turnover缺少合约乘数。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="3c000bba-1277-49d7-abf2-edd53686e135"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1078b863-9e88-4b57-8fa3-c019697eafba"></span>
## 4.FAQ
<p>无</p>
