<p>请求查询签约银行响应，当执行ReqQryContractBank后，该方法被调用。</p>
<span class="anchor" id="39fa0da1-fe37-461a-9b9a-5cbff7bb977f"></span>
## 1.函数原型
<p>virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="0485f1c1-2ae4-4825-b4c6-9540c21bf357"></span>
## 2.参数
<p>pContractBank：查询签约银行响应</p>
<pre><code>struct CThostFtdcContractBankField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///银行代码
    TThostFtdcBankIDType BankID;
    ///银行分中心代码
    TThostFtdcBankBrchIDType BankBrchID;
    ///银行名称
    TThostFtdcBankNameType BankName;
};
</code></pre>
<p>BankID：对应期货公司内部设置的银行编码</p>
<p>BankName：对应期货公司内部设置的银行名称</p>
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
<span class="anchor" id="192cd7fd-853d-4a8b-b7ae-27c5281a14cc"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="696390f7-886e-43f9-89fa-af9416806b97"></span>
## 4.FAQ
<p>无</p>
