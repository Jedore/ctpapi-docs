<p>请求查询组合合约安全系数响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCOMBINSTRUMENTGUARD/">ReqQryCombInstrumentGuard</a>后，该方法被调用。</p>
<span class="anchor" id="a0106faf-2c36-4369-b3a3-9ab96e753251"></span>
## 1.函数原型
<p>virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7ff1f1cb-9fd6-4d43-a5f1-c85aadab2e88"></span>
## 2.参数
<p>pCombInstrumentGuard：组合合约安全系数</p>
<pre><code>struct CThostFtdcCombInstrumentGuardField
{
///经纪公司代码
TThostFtdcBrokerIDType  BrokerID;
///保留的无效字段
TThostFtdcOldInstrumentIDType   reserve1;
///比率类型
TThostFtdcRatioType GuarantRatio;
///交易所代码
TThostFtdcExchangeIDType    ExchangeID;
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
<span class="anchor" id="1b60f125-c5c7-4198-9860-4a72dd3fcd2a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="655752e2-dc88-434a-9e86-16242ae0b13e"></span>
## 4.FAQ
<p>无</p>
