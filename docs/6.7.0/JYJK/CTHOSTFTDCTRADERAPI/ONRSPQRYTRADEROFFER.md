<p>请求查询交易员报盘机响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRADEROFFER/">ReqQryTraderOffer</a>后，该方法被调用。</p>
<span class="anchor" id="e76d967d-19b7-4348-8bb8-dd3dc68d2855"></span>
## 1.函数原型
<p>virtual void OnRspQryTraderOffer(CThostFtdcTraderOfferField *pTraderOffer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2b182b4a-7f76-48ae-806f-0bdb233805f8"></span>
## 2.参数
<p>pTraderOffer：交易所交易员报盘机</p>
<pre><code>struct CThostFtdcTraderOfferField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///交易所交易员代码
    TThostFtdcTraderIDType  TraderID;
    ///会员代码
    TThostFtdcParticipantIDType ParticipantID;
    ///密码
    TThostFtdcPasswordType  Password;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///本地报单编号
    TThostFtdcOrderLocalIDType  OrderLocalID;
    ///交易所交易员连接状态
    TThostFtdcTraderConnectStatusType   TraderConnectStatus;
    ///发出连接请求的日期
    TThostFtdcDateType  ConnectRequestDate;
    ///发出连接请求的时间
    TThostFtdcTimeType  ConnectRequestTime;
    ///上次报告日期
    TThostFtdcDateType  LastReportDate;
    ///上次报告时间
    TThostFtdcTimeType  LastReportTime;
    ///完成连接日期
    TThostFtdcDateType  ConnectDate;
    ///完成连接时间
    TThostFtdcTimeType  ConnectTime;
    ///启动日期
    TThostFtdcDateType  StartDate;
    ///启动时间
    TThostFtdcTimeType  StartTime;
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///本席位最大成交编号
    TThostFtdcTradeIDType   MaxTradeID;
    ///本席位最大报单备拷
    TThostFtdcReturnCodeType    MaxOrderMessageReference;
    ///撤单时选择席位算法
    TThostFtdcOrderCancelAlgType    OrderCancelAlg;
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
<span class="anchor" id="4aeba81d-331c-416c-be4f-45aa08d7308b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="11b9f36f-8769-481f-ab05-3467d72aa63d"></span>
## 4.FAQ
<p>无</p>
