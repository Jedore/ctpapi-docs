<p>取消订阅询价应答，当<a href="../../CTHOSTFTDCMDAPI/UNSUBSCRIBEFORQUOTERSP/">UnSubscribeForQuoteRsp</a>后，调用此接口。</p>
<span class="anchor" id="d283e77b-e140-4ed5-a5f3-38c376416643"></span>
## 1.函数原型
<p>virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="44097be4-2f7a-439f-b4be-88aa6a6818c3"></span>
## 2.参数
<p>pSpecificInstrument：指定的合约</p>
<pre><code>struct CThostFtdcSpecificInstrumentField
{
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
<span class="anchor" id="97691345-c3c2-4efc-8db9-1ace6a72f2e3"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d7dc31f2-106a-4a40-86cc-80950ad983c7"></span>
## 4.FAQ
<p>无</p>
