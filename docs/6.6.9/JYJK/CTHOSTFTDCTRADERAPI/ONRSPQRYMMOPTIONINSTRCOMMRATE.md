<p>请求查询做市商期权合约手续费响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYMMOPTIONINSTRCOMMRATE/">ReqQryMMOptionInstrCommRate</a>后，该方法被调用。</p>
<span class="anchor" id="10ad8c52-e01e-48c6-8fd2-c64b559931b4"></span>
## 1.函数原型
<p>virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0fc41719-952e-4d2e-ba38-17ace799b6b3"></span>
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
<span class="anchor" id="f78ae81b-1175-42b4-abdc-0a400e2b8c6b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f2df38bf-fafa-4b01-b0b0-4979d848c78a"></span>
## 4.FAQ
<p>无</p>
