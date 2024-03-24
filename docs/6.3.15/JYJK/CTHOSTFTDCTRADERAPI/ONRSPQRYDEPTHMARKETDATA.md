<p>请求查询行情响应，当执行ReqQryDepthMarketData后，该方法被调用。</p>
<span class="anchor" id="c273ca6f-9bbf-48be-a606-ad446cda96ba"></span>
## 1.函数原型
<p>virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="4ed48e1a-1955-410e-bd9a-60b0d353ad91"></span>
## 2.参数
<p>pDepthMarketData：深度行情</p>
<pre><code>struct CThostFtdcDepthMarketDataField
{
    ///交易日
    TThostFtdcDateType TradingDay;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///最新价
    TThostFtdcPriceType LastPrice;
    ///上次结算价
    TThostFtdcPriceType PreSettlementPrice;
    ///昨收盘
    TThostFtdcPriceType PreClosePrice;
    ///昨持仓量
    TThostFtdcLargeVolumeType PreOpenInterest;
    ///今开盘
    TThostFtdcPriceType OpenPrice;
    ///最高价
    TThostFtdcPriceType HighestPrice;
    ///最低价
    TThostFtdcPriceType LowestPrice;
    ///数量
    TThostFtdcVolumeType Volume;
    ///成交金额
    TThostFtdcMoneyType Turnover;
    ///持仓量
    TThostFtdcLargeVolumeType OpenInterest;
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
    TThostFtdcTimeType UpdateTime;
    ///最后修改毫秒
    TThostFtdcMillisecType UpdateMillisec;
    ///申买价一
    TThostFtdcPriceType BidPrice1;
    ///申买量一
    TThostFtdcVolumeType BidVolume1;
    ///申卖价一
    TThostFtdcPriceType AskPrice1;
    ///申卖量一
    TThostFtdcVolumeType AskVolume1;
    ///申买价二
    TThostFtdcPriceType BidPrice2;
    ///申买量二
    TThostFtdcVolumeType BidVolume2;
    ///申卖价二
    TThostFtdcPriceType AskPrice2;
    ///申卖量二
    TThostFtdcVolumeType AskVolume2;
    ///申买价三
    TThostFtdcPriceType BidPrice3;
    ///申买量三
    TThostFtdcVolumeType BidVolume3;
    ///申卖价三
    TThostFtdcPriceType AskPrice3;
    ///申卖量三
    TThostFtdcVolumeType AskVolume3;
    ///申买价四
    TThostFtdcPriceType BidPrice4;
    ///申买量四
    TThostFtdcVolumeType BidVolume4;
    ///申卖价四
    TThostFtdcPriceType AskPrice4;
    ///申卖量四
    TThostFtdcVolumeType AskVolume4;
    ///申买价五
    TThostFtdcPriceType BidPrice5;
    ///申买量五
    TThostFtdcVolumeType BidVolume5;
    ///申卖价五
    TThostFtdcPriceType AskPrice5;
    ///申卖量五
    TThostFtdcVolumeType AskVolume5;
    ///当日均价
    TThostFtdcPriceType AveragePrice;
    ///业务日期
    TThostFtdcDateType ActionDay;
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
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="750b389d-872f-46d5-b278-6f73ebd3434d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a339ffce-49cd-4082-943e-064e4377ea9e"></span>
## 4.FAQ
<p>无</p>
