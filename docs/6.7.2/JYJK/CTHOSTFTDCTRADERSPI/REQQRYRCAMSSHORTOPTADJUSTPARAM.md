<p>请求RCAMS空头期权风险调整参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSSHORTOPTADJUSTPARAM/">OnRspQryRCAMSShortOptAdjustParam</a></p>
<span class="anchor" id="c5b988ec-12ae-477b-b737-cc3d20ceac03"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSShortOptAdjustParam(CThostFtdcQryRCAMSShortOptAdjustParamField *pQryRCAMSShortOptAdjustParam, int nRequestID) = 0;</p>
<span class="anchor" id="29be78c4-9864-4f59-8ae8-7df32f7eee2a"></span>
## 2.参数
<p>pQryRCAMSShortOptAdjustParam：RCAMS空头期权风险调整参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">CombProductID</td>
<td style="TEXT-ALIGN: left;">产品组合代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="d0c92238-49f0-49fe-9270-d84243b195c8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="8485946e-837f-4fb3-8e04-334fd9aa2822"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="dd6d7e6e-2f3f-4062-af96-3a08484fca81"></span>
## 5.FAQ
<p>无</p>
