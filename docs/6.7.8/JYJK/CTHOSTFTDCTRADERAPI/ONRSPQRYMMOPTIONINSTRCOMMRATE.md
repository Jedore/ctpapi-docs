<p>请求查询做市商期权合约手续费响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYMMOPTIONINSTRCOMMRATE/">ReqQryMMOptionInstrCommRate</a>后，该方法被调用。</p>
<span class="anchor" id="8da3c376-b892-40f6-af48-9da7ded95392"></span>
## 1.函数原型
<p>virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="92a84fad-a627-41d8-9a00-a749e7f7548f"></span>
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
<span class="anchor" id="159cec72-2e5a-466a-9cd7-fe4c3147c162"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="97b88e55-fc80-48f9-ac7d-68121d97d49f"></span>
## 4.FAQ
<p>无</p>
