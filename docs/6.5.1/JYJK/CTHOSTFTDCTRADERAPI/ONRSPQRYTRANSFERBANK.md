<p>请求查询转帐银行响应，当执行ReqQryTransferBank后，该方法被调用。</p>
<span class="anchor" id="8c24330d-93de-4e3d-82ff-7004c2c6adf6"></span>
## 1.函数原型
<p>virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8e54b150-27fc-4367-aa16-697c6895b1cd"></span>
## 2.参数
<p>pTransferBank：转帐银行</p>
<pre><code>struct CThostFtdcTransferBankField
{
    ///银行代码
    TThostFtdcBankIDType BankID;
    ///银行分中心代码
    TThostFtdcBankBrchIDType BankBrchID;
    ///银行名称
    TThostFtdcBankNameType BankName;
    ///是否活跃
    TThostFtdcBoolType IsActive;
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
<span class="anchor" id="b6d46eda-0bc5-486b-b665-b7f1450681dc"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="297d8fd4-47b5-48d8-9b0d-7aa895fd4bc4"></span>
## 4.FAQ
<p>无</p>
