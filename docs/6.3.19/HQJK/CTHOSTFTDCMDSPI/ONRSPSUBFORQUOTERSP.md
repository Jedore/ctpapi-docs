<p>订阅询价应答，当调用SubscribeForQuoteRsp后，通过此接口返回。</p>
<span class="anchor" id="6c57f019-98f4-4047-acff-801cec7922ee"></span>
## 1.函数原型
<p>virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="9ff858d1-b69d-4b39-bdf6-f9fc4bb03914"></span>
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
<span class="anchor" id="993eaea4-7e16-423f-93ba-0cf5a918834f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="45a8df82-682d-4a58-b864-2a183e32b401"></span>
## 4.FAQ
<p>无</p>
