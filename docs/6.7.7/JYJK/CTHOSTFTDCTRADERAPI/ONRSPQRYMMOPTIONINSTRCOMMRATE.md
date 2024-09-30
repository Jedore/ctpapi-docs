<p>请求查询做市商期权合约手续费响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYMMOPTIONINSTRCOMMRATE/">ReqQryMMOptionInstrCommRate</a>后，该方法被调用。</p>
<span class="anchor" id="20ae0fab-2270-4d80-a621-ba72d1f249b3"></span>
## 1.函数原型
<p>virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="9e52e075-e638-49ff-b413-13f2273d5559"></span>
## 2.参数
<p>pMMOptionInstrCommRate：当前做市商期权合约手续费的详细内容</p>
<pre><code>struct CThostFtdcMMOptionInstrCommRateField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///开仓手续费率
    TThostFtdcRatioType OpenRatioByMoney;
    ///开仓手续费
    TThostFtdcRatioType OpenRatioByVolume;
    ///平仓手续费率
    TThostFtdcRatioType CloseRatioByMoney;
    ///平仓手续费
    TThostFtdcRatioType CloseRatioByVolume;
    ///平今手续费率
    TThostFtdcRatioType CloseTodayRatioByMoney;
    ///平今手续费
    TThostFtdcRatioType CloseTodayRatioByVolume;
    ///执行手续费率
    TThostFtdcRatioType StrikeRatioByMoney;
    ///执行手续费
    TThostFtdcRatioType StrikeRatioByVolume;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<span class="anchor" id="8c183c39-91b9-49be-ae74-b6587cd2411a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d7810916-491b-403a-bc60-3f6905079f17"></span>
## 4.FAQ
<p>无</p>
